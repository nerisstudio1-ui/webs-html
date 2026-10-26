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

/*
 * Importación automática: al activar el tema y, si falta algo (por ejemplo,
 * WooCommerce se activó después), la próxima vez que un administrador entra
 * en el escritorio. Cada parte se marca como hecha para no repetirla.
 */
add_action( 'after_switch_theme', 'maison_auto_import' );
add_action( 'admin_init', 'maison_auto_import', 20 );
function maison_auto_import() {
	if ( wp_doing_ajax() || ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$need_pages    = ! get_option( 'maison_pages_imported' );
	$need_products = class_exists( 'WooCommerce' ) && ! get_option( 'maison_products_imported' );
	if ( ! $need_pages && ! $need_products ) {
		return;
	}
	// Evita que dos pestañas importen a la vez.
	if ( get_transient( 'maison_import_lock' ) ) {
		return;
	}
	set_transient( 'maison_import_lock', 1, 5 * MINUTE_IN_SECONDS );
	$log = maison_do_import( $need_pages, $need_products );
	delete_transient( 'maison_import_lock' );
	set_transient( 'maison_import_log', $log, HOUR_IN_SECONDS );
}

/**
 * Ejecuta la importación y devuelve un registro legible.
 * Los errores se capturan para no romper el escritorio.
 */
function maison_do_import( $pages_too = true, $products_too = true ) {
	require_once ABSPATH . 'wp-admin/includes/image.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 300 ); // phpcs:ignore WordPress.PHP.NoSilencedErrors
	}

	$log = array();
	try {
		if ( $pages_too ) {
			$pages = maison_import_pages( $log );
			maison_import_menus( $pages, $log );
			update_option( 'maison_pages_imported', 1 );
		}
		if ( $products_too && class_exists( 'WooCommerce' ) ) {
			maison_import_products( $log );
			// El menú se creó antes que la tienda: corrige el enlace "Producto".
			maison_fix_shop_menu_items();
			update_option( 'maison_products_imported', 1 );
		}
		update_option( 'maison_imported', 1 );
		flush_rewrite_rules();
	} catch ( Throwable $e ) {
		$log[] = '<strong>Error:</strong> ' . esc_html( $e->getMessage() );
		update_option( 'maison_import_error', $e->getMessage() );
	}
	return $log;
}

/** Sustituye los enlaces provisionales del menú por la página de la tienda. */
function maison_fix_shop_menu_items() {
	$shop = function_exists( 'wc_get_page_id' ) ? wc_get_page_id( 'shop' ) : 0;
	if ( $shop <= 0 ) {
		return;
	}
	foreach ( array( 'Menú principal', 'Pie · Maison' ) as $name ) {
		$menu = wp_get_nav_menu_object( $name );
		if ( ! $menu ) {
			continue;
		}
		foreach ( (array) wp_get_nav_menu_items( $menu->term_id ) as $item ) {
			if ( 'custom' === $item->type && in_array( $item->title, array( 'Producto', 'Equipamiento' ), true ) ) {
				wp_update_nav_menu_item(
					$menu->term_id,
					$item->ID,
					array(
						'menu-item-title'     => $item->title,
						'menu-item-object'    => 'page',
						'menu-item-object-id' => $shop,
						'menu-item-type'      => 'post_type',
						'menu-item-status'    => 'publish',
						'menu-item-position'  => $item->menu_order,
					)
				);
			}
		}
	}
}

add_action( 'admin_notices', 'maison_importer_notice' );
function maison_importer_notice() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$screen = get_current_screen();
	if ( $screen && 'appearance_page_maison-setup' === $screen->id ) {
		return;
	}
	$log = get_transient( 'maison_import_log' );
	if ( $log ) {
		delete_transient( 'maison_import_log' );
		printf(
			'<div class="notice notice-success is-dismissible"><p><strong>%s</strong><br>%s</p></div>',
			esc_html__( 'Maison Reformer: contenido importado.', 'maison' ),
			wp_kses_post( implode( '<br>', $log ) )
		);
	}
	if ( ! class_exists( 'WooCommerce' ) && ! get_option( 'maison_products_imported' ) ) {
		printf(
			'<div class="notice notice-warning"><p>%s</p></div>',
			esc_html__( 'Maison Reformer: instala y activa WooCommerce para que se creen los productos automáticamente.', 'maison' )
		);
	}
}

function maison_importer_page() {
	$log = get_transient( 'maison_import_log' );
	delete_transient( 'maison_import_log' );
	$err = get_option( 'maison_import_error' );
	?>
	<div class="wrap">
		<h1><?php esc_html_e( 'Maison Reformer · Contenido inicial', 'maison' ); ?></h1>
		<table class="widefat striped" style="max-width:640px;margin:20px 0">
			<tbody>
				<tr><td><?php esc_html_e( 'Páginas, menús y portada', 'maison' ); ?></td><td><?php echo get_option( 'maison_pages_imported' ) ? '✅ ' . esc_html__( 'Importado', 'maison' ) : '— ' . esc_html__( 'Pendiente', 'maison' ); ?></td></tr>
				<tr><td><?php esc_html_e( 'WooCommerce', 'maison' ); ?></td><td><?php echo class_exists( 'WooCommerce' ) ? '✅ ' . esc_html__( 'Activo', 'maison' ) : '⚠️ ' . esc_html__( 'No está activo', 'maison' ); ?></td></tr>
				<tr><td><?php esc_html_e( 'Categorías y 7 productos', 'maison' ); ?></td><td><?php echo get_option( 'maison_products_imported' ) ? '✅ ' . esc_html__( 'Importado', 'maison' ) : '— ' . esc_html__( 'Pendiente', 'maison' ); ?></td></tr>
			</tbody>
		</table>
		<?php if ( $err ) : ?>
			<div class="notice notice-error"><p><?php echo esc_html( sprintf( /* translators: %s: error */ __( 'Último error al importar: %s', 'maison' ), $err ) ); ?></p></div>
		<?php endif; ?>
		<?php if ( $log ) : ?>
			<div class="notice notice-success"><p><?php echo wp_kses_post( implode( '<br>', $log ) ); ?></p></div>
		<?php endif; ?>
		<p><?php esc_html_e( 'El botón vuelve a comprobar todo y crea lo que falte (páginas, menús, categorías y productos). Lo que ya existe no se duplica ni se sobrescribe.', 'maison' ); ?></p>
		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="maison_import">
			<?php wp_nonce_field( 'maison_import' ); ?>
			<?php submit_button( __( 'Importar / completar contenido', 'maison' ) ); ?>
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
	delete_option( 'maison_import_error' );
	$log = maison_do_import( true, true );
	if ( ! $log ) {
		$log[] = __( 'Todo estaba ya creado: no había nada nuevo que importar.', 'maison' );
	}
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
