<?php
/**
 * Integración con WooCommerce: catálogo, ficha de producto al estilo Maison,
 * "Precio por confirmar", campos de Accesorios / Ficha técnica y carrito.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

/* ---------------------------------------------------------------------------
 * General
 * ------------------------------------------------------------------------- */

// Quitamos los envoltorios y migas por defecto: el tema pone los suyos.
remove_action( 'woocommerce_before_main_content', 'woocommerce_output_content_wrapper', 10 );
remove_action( 'woocommerce_after_main_content', 'woocommerce_output_content_wrapper_end', 10 );
remove_action( 'woocommerce_before_main_content', 'woocommerce_breadcrumb', 20 );
remove_action( 'woocommerce_sidebar', 'woocommerce_get_sidebar', 10 );
add_filter( 'woocommerce_show_page_title', '__return_false' );
// La descripción de la categoría ya se muestra en la cabecera del tema (woocommerce.php).
remove_action( 'woocommerce_archive_description', 'woocommerce_taxonomy_archive_description', 10 );
remove_action( 'woocommerce_archive_description', 'woocommerce_product_archive_description', 10 );

// Catálogo limpio: sin contador de resultados ni ordenación.
remove_action( 'woocommerce_before_shop_loop', 'woocommerce_result_count', 20 );
remove_action( 'woocommerce_before_shop_loop', 'woocommerce_catalog_ordering', 30 );

// Tarjeta de producto: sin botón ni valoraciones, con la categoría bajo el nombre.
remove_action( 'woocommerce_after_shop_loop_item', 'woocommerce_template_loop_add_to_cart', 10 );
remove_action( 'woocommerce_after_shop_loop_item_title', 'woocommerce_template_loop_rating', 5 );
add_action( 'woocommerce_after_shop_loop_item_title', 'maison_loop_category', 5 );
function maison_loop_category() {
	global $product;
	$terms = get_the_terms( $product->get_id(), 'product_cat' );
	if ( $terms && ! is_wp_error( $terms ) ) {
		echo '<span class="loop-cat">' . esc_html( $terms[0]->name ) . '</span>';
	}
}

// Miniaturas sin recortar y con resolución suficiente para pantallas retina.
add_filter( 'woocommerce_get_image_size_thumbnail', 'maison_thumbnail_size' );
function maison_thumbnail_size( $size ) {
	return array(
		'width'  => 1000,
		'height' => 0,
		'crop'   => 0,
	);
}
add_filter( 'woocommerce_get_image_size_single', 'maison_single_size' );
function maison_single_size( $size ) {
	return array(
		'width'  => 1600,
		'height' => 0,
		'crop'   => 0,
	);
}

add_filter( 'loop_shop_columns', 'maison_loop_columns' );
function maison_loop_columns() {
	return 4;
}

/* ---------------------------------------------------------------------------
 * Precio por confirmar
 * ------------------------------------------------------------------------- */

add_filter( 'woocommerce_empty_price_html', 'maison_empty_price' );
add_filter( 'woocommerce_variable_empty_price_html', 'maison_empty_price' );
function maison_empty_price() {
	return '<span class="price-tbc">' . esc_html__( 'Precio por confirmar', 'maison' ) . '</span>';
}

/** True si el producto aún no tiene precio y, por tanto, se pide presupuesto. */
function maison_is_quote_only( $product ) {
	return $product && '' === $product->get_price();
}

/* ---------------------------------------------------------------------------
 * Ficha de producto
 * ------------------------------------------------------------------------- */

remove_action( 'woocommerce_single_product_summary', 'woocommerce_template_single_rating', 10 );
remove_action( 'woocommerce_single_product_summary', 'woocommerce_template_single_excerpt', 20 );
remove_action( 'woocommerce_single_product_summary', 'woocommerce_template_single_meta', 40 );
remove_action( 'woocommerce_after_single_product_summary', 'woocommerce_output_product_data_tabs', 10 );

add_action( 'woocommerce_single_product_summary', 'maison_single_crumbs', 1 );
function maison_single_crumbs() {
	woocommerce_breadcrumb(
		array(
			'delimiter'   => ' / ',
			'wrap_before' => '<nav class="crumbs">',
			'wrap_after'  => '</nav>',
			'home'        => false,
		)
	);
}

add_action( 'woocommerce_single_product_summary', 'maison_price_note', 11 );
function maison_price_note() {
	echo '<p class="vat">' . esc_html__( '+ IVA · Envío gratuito a península', 'maison' ) . '</p><hr>';
}

// Sin precio: en lugar del carrito, botón para pedir presupuesto.
add_action( 'woocommerce_before_single_product', 'maison_maybe_quote_mode' );
function maison_maybe_quote_mode() {
	global $product;
	if ( maison_is_quote_only( $product ) ) {
		remove_action( 'woocommerce_single_product_summary', 'woocommerce_template_single_add_to_cart', 30 );
		add_action( 'woocommerce_single_product_summary', 'maison_quote_button', 30 );
	}
}

function maison_quote_button() {
	global $product;
	$colors   = maison_product_colors( $product );
	$defaults = $product->get_default_attributes();
	$current  = isset( $defaults['color'] ) && in_array( $defaults['color'], $colors, true ) ? $defaults['color'] : ( $colors ? $colors[0] : '' );

	echo '<div class="quote-form" data-quote-form data-product="' . esc_attr( $product->get_name() ) . '" data-url="' . esc_url( maison_page_url( 'contacto' ) ) . '">';
	if ( $colors ) {
		echo '<div class="label">' . esc_html__( 'Color', 'maison' ) . ': <span data-quote-color>' . esc_html( $current ) . '</span></div>';
		echo '<div class="swatches" role="group" aria-label="' . esc_attr__( 'Color de tapizado', 'maison' ) . '">';
		foreach ( $colors as $color ) {
			printf(
				'<button type="button" class="swatch" data-quote-swatch="%1$s" aria-pressed="%2$s"><i style="background:%3$s"></i>%4$s</button>',
				esc_attr( $color ),
				$color === $current ? 'true' : 'false',
				esc_attr( maison_swatch_color( $color ) ),
				esc_html( $color )
			);
		}
		echo '</div>';
	}
	echo '<div class="quote-row">';
	echo '<div class="quantity"><input type="number" class="input-text qty text" value="1" min="1" step="1" inputmode="numeric" aria-label="' . esc_attr__( 'Cantidad', 'maison' ) . '" data-quote-qty></div>';
	printf(
		'<a class="btn quote-btn" data-quote-link href="%s">%s</a>',
		esc_url( maison_contact_url( sprintf( /* translators: %s: producto */ __( 'Presupuesto · %s', 'maison' ), $product->get_name() ) ) ),
		esc_html__( 'Solicitar presupuesto', 'maison' )
	);
	echo '</div></div>';
}

/** Colores de tapizado del producto (atributo "Color"). */
function maison_product_colors( $product ) {
	foreach ( $product->get_attributes() as $attribute ) {
		$name = $attribute->is_taxonomy() ? wc_attribute_label( $attribute->get_name() ) : $attribute->get_name();
		if ( 'color' === sanitize_title( $name ) ) {
			return $attribute->is_taxonomy()
				? wc_get_product_terms( $product->get_id(), $attribute->get_name(), array( 'fields' => 'names' ) )
				: $attribute->get_options();
		}
	}
	return array();
}

/** Color de muestra para cada acabado. */
function maison_swatch_color( $name ) {
	$map = array(
		'negro'  => '#1d1b1a',
		'gris'   => '#9a9894',
		'mocca'  => '#8a6e5c',
		'moca'   => '#8a6e5c',
		'blanco' => '#f4f1ec',
		'beige'  => '#d9c8b4',
	);
	$key = sanitize_title( $name );
	return isset( $map[ $key ] ) ? $map[ $key ] : '#cfc6bc';
}

// Pasamos los colores al JS para pintar los selectores de variación como muestras.
add_action( 'wp_footer', 'maison_swatch_map' );
function maison_swatch_map() {
	if ( ! is_product() ) {
		return;
	}
	$map = array();
	foreach ( array( 'Negro', 'Gris', 'Mocca', 'Blanco', 'Beige' ) as $color ) {
		$map[ sanitize_title( $color ) ] = maison_swatch_color( $color );
	}
	echo '<script>window.MAISON_SWATCHES=' . wp_json_encode( $map ) . ';</script>';
}

add_action( 'woocommerce_single_product_summary', 'maison_after_cart', 35 );
function maison_after_cart() {
	global $product;
	if ( ! $product instanceof WC_Product ) {
		return;
	}
	$whatsapp = preg_replace( '/\D/', '', maison_mod( 'whatsapp' ) );
	$chat_url = $whatsapp
		? 'https://wa.me/' . $whatsapp . '?text=' . rawurlencode( sprintf( 'Hola, me interesa %s.', $product->get_name() ) )
		: maison_contact_url( sprintf( 'Consulta · %s', $product->get_name() ) );

	echo '<p class="ship">' . esc_html__( 'Fecha prevista de envío: por confirmar', 'maison' ) . '</p>';
	printf(
		'<a class="btn btn-line btn-block chat" href="%s"%s>%s</a>',
		esc_url( $chat_url ),
		$whatsapp ? ' target="_blank" rel="noopener"' : '',
		esc_html__( 'Chatea con nosotros', 'maison' )
	);
	maison_product_accordion();
}

/** Muestra las pestañas de WooCommerce como acordeón bajo el botón de compra. */
function maison_product_accordion() {
	$tabs = apply_filters( 'woocommerce_product_tabs', array() );
	if ( ! $tabs ) {
		return;
	}
	echo '<div class="acc">';
	$first = true;
	foreach ( $tabs as $key => $tab ) {
		if ( empty( $tab['callback'] ) ) {
			continue;
		}
		printf( '<details%s><summary>%s</summary><div class="body">', $first ? ' open' : '', wp_kses_post( apply_filters( 'woocommerce_product_' . $key . '_tab_title', $tab['title'], $key ) ) );
		call_user_func( $tab['callback'], $key, $tab );
		echo '</div></details>';
		$first = false;
	}
	echo '</div>';
}

add_filter( 'woocommerce_product_description_heading', '__return_empty_string' );
add_filter( 'woocommerce_product_additional_information_heading', '__return_empty_string' );

add_filter( 'woocommerce_product_tabs', 'maison_product_tabs', 20 );
function maison_product_tabs( $tabs ) {
	global $product;
	if ( ! $product instanceof WC_Product ) {
		return $tabs;
	}

	if ( isset( $tabs['description'] ) ) {
		$tabs['description']['title'] = __( 'Descripción', 'maison' );
	}
	if ( isset( $tabs['additional_information'] ) ) {
		$tabs['additional_information']['title']    = __( 'Características', 'maison' );
		$tabs['additional_information']['priority'] = 25;
	}

	if ( get_post_meta( $product->get_id(), '_maison_accessories', true ) ) {
		$tabs['maison_accessories'] = array(
			'title'    => __( 'Accesorios incluidos', 'maison' ),
			'priority' => 15,
			'callback' => 'maison_tab_accessories',
		);
	}
	$tabs['maison_sheet']    = array(
		'title'    => __( 'Ficha técnica · Medidas y características', 'maison' ),
		'priority' => 30,
		'callback' => 'maison_tab_sheet',
	);
	$tabs['maison_care']     = array(
		'title'    => __( 'Cuidados y mantenimiento', 'maison' ),
		'priority' => 40,
		'callback' => 'maison_tab_care',
	);
	$tabs['maison_shipping'] = array(
		'title'    => __( 'Envíos y entregas', 'maison' ),
		'priority' => 50,
		'callback' => 'maison_tab_shipping',
	);
	return $tabs;
}

function maison_tab_accessories() {
	global $product;
	if ( ! $product instanceof WC_Product ) {
		return;
	}
	$items = array_filter( array_map( 'trim', explode( "\n", (string) get_post_meta( $product->get_id(), '_maison_accessories', true ) ) ) );
	echo '<ul class="chips">';
	foreach ( $items as $item ) {
		echo '<li>' . esc_html( $item ) . '</li>';
	}
	echo '</ul>';
}

function maison_tab_sheet() {
	global $product;
	$pdf = get_post_meta( $product->get_id(), '_maison_sheet_pdf', true );
	if ( $pdf ) {
		printf( '<p><a href="%s" target="_blank" rel="noopener" download>%s</a></p>', esc_url( $pdf ), esc_html__( 'Descargar PDF →', 'maison' ) );
		return;
	}
	echo '<p>' . esc_html__( 'La ficha técnica completa estará disponible próximamente. Si necesitas las medidas o características del equipo, escríbenos y te la enviamos.', 'maison' ) . '</p>';
	printf(
		'<p><a href="%s">%s</a></p>',
		esc_url( maison_contact_url( 'Ficha técnica · ' . $product->get_name() ) ),
		esc_html__( 'Solicitar ficha técnica →', 'maison' )
	);
}

function maison_tab_care() {
	echo '<p>' . esc_html__( 'Mantén tu equipo en un espacio interior, protegido de la humedad. Limpia guías y raíles semanalmente, la tapicería después de cada uso con un paño de microfibra ligeramente humedecido y revisa periódicamente muelles, mosquetones y enganches.', 'maison' ) . '</p>';
	printf( '<p><a href="%s">%s</a></p>', esc_url( maison_page_url( 'maison-care' ) ), esc_html__( 'Ver la guía Maison Care →', 'maison' ) );
}

function maison_tab_shipping() {
	echo '<p>' . esc_html__( 'Envío estándar gratuito a España peninsular, con entrega a pie de calle en 24-48 horas laborables para productos en stock. Entrega interior y montaje disponibles bajo presupuesto.', 'maison' ) . '</p>';
	printf( '<p><a href="%s">%s</a></p>', esc_url( maison_page_url( 'envios' ) ), esc_html__( 'Política de envíos y entregas →', 'maison' ) );
}

add_filter( 'woocommerce_product_related_products_heading', 'maison_related_heading' );
function maison_related_heading() {
	return __( 'También te puede gustar', 'maison' );
}

add_filter( 'woocommerce_output_related_products_args', 'maison_related_args' );
function maison_related_args( $args ) {
	$args['posts_per_page'] = 3;
	$args['columns']        = 3;
	return $args;
}

/* ---------------------------------------------------------------------------
 * Campos extra en la edición del producto (pestaña General)
 * ------------------------------------------------------------------------- */

add_action( 'woocommerce_product_options_general_product_data', 'maison_product_fields' );
function maison_product_fields() {
	echo '<div class="options_group">';
	woocommerce_wp_textarea_input(
		array(
			'id'          => '_maison_accessories',
			'label'       => __( 'Accesorios incluidos', 'maison' ),
			'description' => __( 'Uno por línea. Se muestra en la ficha como "Accesorios incluidos".', 'maison' ),
			'desc_tip'    => true,
			'rows'        => 6,
		)
	);
	woocommerce_wp_text_input(
		array(
			'id'          => '_maison_sheet_pdf',
			'label'       => __( 'Ficha técnica (URL del PDF)', 'maison' ),
			'description' => __( 'Sube el PDF a Medios y pega aquí su URL.', 'maison' ),
			'desc_tip'    => true,
			'type'        => 'url',
		)
	);
	echo '</div>';
}

add_action( 'woocommerce_admin_process_product_object', 'maison_save_product_fields' );
function maison_save_product_fields( $product ) {
	// phpcs:disable WordPress.Security.NonceVerification.Missing -- WooCommerce verifica el nonce del formulario de producto.
	if ( isset( $_POST['_maison_accessories'] ) ) {
		$product->update_meta_data( '_maison_accessories', sanitize_textarea_field( wp_unslash( $_POST['_maison_accessories'] ) ) );
	}
	if ( isset( $_POST['_maison_sheet_pdf'] ) ) {
		$product->update_meta_data( '_maison_sheet_pdf', esc_url_raw( wp_unslash( $_POST['_maison_sheet_pdf'] ) ) );
	}
	// phpcs:enable
}

/* ---------------------------------------------------------------------------
 * Contador del carrito en la cabecera
 * ------------------------------------------------------------------------- */

add_filter( 'woocommerce_add_to_cart_fragments', 'maison_cart_fragment' );
function maison_cart_fragment( $fragments ) {
	$count = WC()->cart->get_cart_contents_count();
	$fragments['span[data-cart-count]'] = '<span class="cart-count" data-cart-count>' . ( $count ? esc_html( $count ) : '' ) . '</span>';
	return $fragments;
}
