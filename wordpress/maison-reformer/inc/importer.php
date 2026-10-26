<?php
/**
 * Importador de contenido inicial: Apariencia → Maison Reformer.
 * Crea las páginas con los textos del briefing, los menús y, si WooCommerce
 * está activo, las categorías y los 7 productos con sus fotos.
 * Es seguro ejecutarlo varias veces: lo que ya existe no se duplica.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

add_action( 'admin_menu', 'maison_importer_menu' );
function maison_importer_menu() {
	add_theme_page( __( 'Maison Reformer', 'maison' ), __( 'Maison Reformer', 'maison' ), 'manage_options', 'maison-setup', 'maison_importer_page' );
}

add_action( 'admin_notices', 'maison_importer_notice' );
function maison_importer_notice() {
	if ( get_option( 'maison_imported' ) || ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$screen = get_current_screen();
	if ( $screen && 'appearance_page_maison-setup' === $screen->id ) {
		return;
	}
	printf(
		'<div class="notice notice-info"><p>%s <a class="button button-primary" href="%s">%s</a></p></div>',
		esc_html__( 'Tema Maison Reformer activado. Importa las páginas, menús y productos para empezar.', 'maison' ),
		esc_url( admin_url( 'themes.php?page=maison-setup' ) ),
		esc_html__( 'Importar contenido', 'maison' )
	);
}

function maison_importer_page() {
	$log = get_transient( 'maison_import_log' );
	delete_transient( 'maison_import_log' );
	?>
	<div class="wrap">
		<h1><?php esc_html_e( 'Maison Reformer · Contenido inicial', 'maison' ); ?></h1>
		<p><?php esc_html_e( 'Crea las páginas (Inicio, Sobre nosotros, FAQs, Contacto, Envíos, Garantía, Devoluciones, Maison Care y Privacidad), los menús y la portada.', 'maison' ); ?></p>
		<?php if ( class_exists( 'WooCommerce' ) ) : ?>
			<p><?php esc_html_e( 'También crea las categorías y los 7 productos (The Icon, The Maison, The Cadillac, Wunda Chair, Ladder Barrel, Spine Corrector y Wall Tower) con sus fotos, colores y descripciones. Los precios quedan vacíos ("Precio por confirmar") hasta que los rellenes.', 'maison' ); ?></p>
		<?php else : ?>
			<p><strong><?php esc_html_e( 'Activa WooCommerce antes de importar para que se creen también los productos.', 'maison' ); ?></strong></p>
		<?php endif; ?>
		<?php if ( $log ) : ?>
			<div class="notice notice-success"><p><?php echo wp_kses_post( implode( '<br>', $log ) ); ?></p></div>
		<?php endif; ?>
		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="maison_import">
			<?php wp_nonce_field( 'maison_import' ); ?>
			<?php submit_button( __( 'Importar contenido', 'maison' ) ); ?>
		</form>
	</div>
	<?php
}

add_action( 'admin_post_maison_import', 'maison_run_import' );
function maison_run_import() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( esc_html__( 'No tienes permisos.', 'maison' ) );
	}
	check_admin_referer( 'maison_import' );

	require_once ABSPATH . 'wp-admin/includes/image.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';

	$log   = array();
	$pages = maison_import_pages( $log );
	maison_import_menus( $pages, $log );
	if ( class_exists( 'WooCommerce' ) ) {
		maison_import_products( $log );
	}
	update_option( 'maison_imported', 1 );
	flush_rewrite_rules();

	set_transient( 'maison_import_log', $log, 300 );
	wp_safe_redirect( admin_url( 'themes.php?page=maison-setup' ) );
	exit;
}

/** Sube una imagen del tema a la biblioteca de medios (una sola vez). */
function maison_import_image( $file, $title ) {
	$existing = get_posts(
		array(
			'post_type'   => 'attachment',
			'post_status' => 'inherit',
			'meta_key'    => '_maison_source', // phpcs:ignore WordPress.DB.SlowDBQuery
			'meta_value'  => $file, // phpcs:ignore WordPress.DB.SlowDBQuery
			'numberposts' => 1,
			'fields'      => 'ids',
		)
	);
	if ( $existing ) {
		return $existing[0];
	}
	$tmp = wp_tempnam( $file );
	copy( MAISON_DIR . '/assets/img/' . $file, $tmp );
	$id = media_handle_sideload( array( 'name' => $file, 'tmp_name' => $tmp ), 0, $title );
	if ( is_wp_error( $id ) ) {
		wp_delete_file( $tmp );
		return 0;
	}
	update_post_meta( $id, '_maison_source', $file );
	return $id;
}

/** Contenido de una página guardado en inc/content, con los enlaces internos resueltos. */
function maison_content( $slug ) {
	$path = MAISON_DIR . '/inc/content/' . $slug . '.html';
	if ( ! file_exists( $path ) ) {
		return '';
	}
	$html = file_get_contents( $path ); // phpcs:ignore WordPress.WP.AlternativeFunctions
	return preg_replace_callback(
		'/\{\{([a-z-]+)\}\}/',
		function ( $m ) {
			return esc_url( maison_page_url( $m[1] ) );
		},
		$html
	);
}

function maison_import_pages( &$log ) {
	$defs = array(
		'inicio'         => array( 'Inicio', '', '' ),
		'sobre-nosotros' => array( 'Sobre nosotros', '', '' ),
		'faqs'           => array( 'Preguntas frecuentes', 'Todo lo que necesitas saber antes y después de tu compra.', '' ),
		'contacto'       => array( 'Contacto', '', 'page-templates/template-contacto.php' ),
		'envios'         => array( 'Política de envíos y entregas', '', '' ),
		'garantia'       => array( 'Garantía', '', '' ),
		'devoluciones'   => array( 'Política de devoluciones', '', '' ),
		'maison-care'    => array( 'Maison Care', 'Para garantizar el correcto funcionamiento, la seguridad y la durabilidad de tu equipo, en Maison Reformer recomendamos seguir estas pautas.', '' ),
		'privacidad'     => array( 'Política de privacidad', '', '' ),
	);
	$ids  = array();
	// Primero se crean todas las páginas para que los enlaces internos del contenido se resuelvan.
	foreach ( $defs as $slug => $def ) {
		$page = get_page_by_path( $slug );
		if ( $page ) {
			$ids[ $slug ] = $page->ID;
			continue;
		}
		$ids[ $slug ] = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => $def[0],
				'post_name'    => $slug,
				'post_excerpt' => $def[1],
			)
		);
		if ( $def[2] ) {
			update_post_meta( $ids[ $slug ], '_wp_page_template', $def[2] );
		}
		$log[] = sprintf( 'Página creada: %s', $def[0] );
	}
	foreach ( $ids as $slug => $id ) {
		$post = get_post( $id );
		if ( $post && '' === $post->post_content && maison_content( $slug ) ) {
			wp_update_post( array( 'ID' => $id, 'post_content' => maison_content( $slug ) ) );
		}
	}

	if ( ! has_post_thumbnail( $ids['sobre-nosotros'] ) ) {
		$img = maison_import_image( 'the-icon.jpg', 'Reformer The Icon' );
		if ( $img ) {
			set_post_thumbnail( $ids['sobre-nosotros'], $img );
		}
	}

	update_option( 'show_on_front', 'page' );
	update_option( 'page_on_front', $ids['inicio'] );
	update_option( 'wp_page_for_privacy_policy', $ids['privacidad'] );
	$log[] = 'Portada asignada a la página Inicio.';
	return $ids;
}

function maison_import_menus( $pages, &$log ) {
	$shop = function_exists( 'wc_get_page_id' ) ? wc_get_page_id( 'shop' ) : 0;
	$menus = array(
		'primary'      => array(
			'name'  => 'Menú principal',
			'items' => array( 'inicio' => 'Inicio', 'shop' => 'Producto', 'sobre-nosotros' => 'Sobre nosotros', 'faqs' => 'FAQs', 'contacto' => 'Contacto' ),
		),
		'footer_info'  => array(
			'name'  => 'Pie · Información',
			'items' => array( 'envios' => 'Política de envíos y entregas', 'garantia' => 'Garantía', 'devoluciones' => 'Política de devoluciones', 'contacto' => 'Contacto' ),
		),
		'footer_house' => array(
			'name'  => 'Pie · Maison',
			'items' => array( 'shop' => 'Equipamiento', 'sobre-nosotros' => 'Sobre nosotros', 'faqs' => 'FAQs', 'maison-care' => 'Maison Care' ),
		),
	);
	$locations = get_theme_mod( 'nav_menu_locations', array() );
	foreach ( $menus as $location => $menu ) {
		if ( wp_get_nav_menu_object( $menu['name'] ) ) {
			continue;
		}
		$menu_id = wp_create_nav_menu( $menu['name'] );
		if ( is_wp_error( $menu_id ) ) {
			continue;
		}
		foreach ( $menu['items'] as $slug => $label ) {
			$object_id = 'shop' === $slug ? $shop : ( isset( $pages[ $slug ] ) ? $pages[ $slug ] : 0 );
			if ( $object_id > 0 ) {
				wp_update_nav_menu_item(
					$menu_id,
					0,
					array(
						'menu-item-title'     => $label,
						'menu-item-object'    => 'page',
						'menu-item-object-id' => $object_id,
						'menu-item-type'      => 'post_type',
						'menu-item-status'    => 'publish',
					)
				);
			} elseif ( 'shop' === $slug ) {
				wp_update_nav_menu_item(
					$menu_id,
					0,
					array(
						'menu-item-title'  => $label,
						'menu-item-url'    => home_url( '/' ),
						'menu-item-type'   => 'custom',
						'menu-item-status' => 'publish',
					)
				);
			}
		}
		$locations[ $location ] = $menu_id;
		$log[]                  = sprintf( 'Menú creado: %s', $menu['name'] );
	}
	set_theme_mod( 'nav_menu_locations', $locations );
}

function maison_import_products( &$log ) {
	$shop = wc_get_page_id( 'shop' );
	if ( $shop > 0 ) {
		wp_update_post( array( 'ID' => $shop, 'post_title' => 'Equipamiento' ) );
	}

	$cats   = array(
		'reformers'       => 'Reformers',
		'reformers-torre' => 'Reformers con torre',
		'cadillacs'       => 'Cadillacs',
		'wunda-chair'     => 'Wunda Chair',
		'barrel-spine'    => 'Barrel y Spine',
		'wall-tower'      => 'Wall Tower',
	);
	$cat_id = array();
	$order  = 0;
	foreach ( $cats as $slug => $name ) {
		$term = get_term_by( 'slug', $slug, 'product_cat' );
		if ( ! $term ) {
			$res  = wp_insert_term( $name, 'product_cat', array( 'slug' => $slug ) );
			$term = is_wp_error( $res ) ? null : get_term( $res['term_id'], 'product_cat' );
		}
		if ( $term ) {
			$cat_id[ $slug ] = $term->term_id;
			update_term_meta( $term->term_id, 'order', $order++ );
		}
	}

	$data = json_decode( file_get_contents( MAISON_DIR . '/inc/content/products.json' ), true ); // phpcs:ignore WordPress.WP.AlternativeFunctions
	foreach ( $data as $i => $p ) {
		if ( get_page_by_path( $p['slug'], OBJECT, 'product' ) ) {
			continue;
		}
		$product = $p['colors'] ? new WC_Product_Variable() : new WC_Product_Simple();
		$product->set_name( $p['name'] );
		$product->set_slug( $p['slug'] );
		$product->set_status( 'publish' );
		$product->set_menu_order( $i );
		$product->set_description( '<p>' . implode( "</p>\n<p>", array_map( 'esc_html', $p['description'] ) ) . '</p>' );
		$product->set_short_description( esc_html( $p['description'][0] ) );
		if ( isset( $cat_id[ $p['category'] ] ) ) {
			$product->set_category_ids( array( $cat_id[ $p['category'] ] ) );
		}
		$image = maison_import_image( $p['image'], $p['name'] );
		if ( $image ) {
			$product->set_image_id( $image );
		}
		if ( $p['colors'] ) {
			$attribute = new WC_Product_Attribute();
			$attribute->set_name( 'Color' );
			$attribute->set_options( $p['colors'] );
			$attribute->set_visible( true );
			$attribute->set_variation( true );
			$product->set_attributes( array( $attribute ) );
			$product->set_default_attributes( array( 'color' => $p['default_color'] ) );
		}
		if ( ! empty( $p['accessories'] ) ) {
			$product->update_meta_data( '_maison_accessories', implode( "\n", $p['accessories'] ) );
		}
		$product_id = $product->save();

		foreach ( $p['colors'] as $color ) {
			$variation = new WC_Product_Variation();
			$variation->set_parent_id( $product_id );
			$variation->set_attributes( array( 'color' => $color ) );
			$variation->set_status( 'publish' );
			$variation->save();
		}
		if ( $p['colors'] ) {
			WC_Product_Variable::sync( $product_id );
		}
		$log[] = sprintf( 'Producto creado: %s', $p['name'] );
	}
}
