<?php
/**
 * Configuración básica del tema: soportes, menús, estilos y utilidades.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', 'maison_setup' );
function maison_setup() {
	load_theme_textdomain( 'maison', MAISON_DIR . '/languages' );
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' ) );
	add_theme_support( 'responsive-embeds' );
	add_theme_support(
		'woocommerce',
		array(
			'thumbnail_image_width' => 1000,
			'single_image_width'    => 1600,
			'product_grid'          => array( 'default_columns' => 4, 'default_rows' => 3 ),
		)
	);
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );

	register_nav_menus(
		array(
			'primary'      => __( 'Menú principal', 'maison' ),
			'footer_info'  => __( 'Pie · Información', 'maison' ),
			'footer_house' => __( 'Pie · Maison', 'maison' ),
		)
	);
}

add_action( 'init', 'maison_page_excerpts' );
function maison_page_excerpts() {
	// El extracto de una página se muestra como subtítulo bajo el título.
	add_post_type_support( 'page', 'excerpt' );
}

add_action( 'wp_enqueue_scripts', 'maison_assets' );
function maison_assets() {
	wp_enqueue_style(
		'maison-fonts',
		'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200;0,6..72,300;1,6..72,200&family=Montserrat:wght@300;400;500&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'maison', get_stylesheet_uri(), array( 'maison-fonts' ), MAISON_VERSION );
	wp_enqueue_script( 'maison', MAISON_URI . '/assets/js/main.js', array(), MAISON_VERSION, true );
}

add_filter( 'wp_resource_hints', 'maison_resource_hints', 10, 2 );
function maison_resource_hints( $urls, $relation ) {
	if ( 'preconnect' === $relation ) {
		$urls[] = 'https://fonts.googleapis.com';
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
	}
	return $urls;
}

add_filter( 'body_class', 'maison_body_class' );
function maison_body_class( $classes ) {
	if ( is_front_page() ) {
		$classes[] = 'home';
	}
	return $classes;
}

/** URL de una imagen incluida en el tema. */
function maison_img( $file ) {
	return MAISON_URI . '/assets/img/' . $file;
}

/** URL de una página por su slug, con alternativa si no existe. */
function maison_page_url( $slug, $fallback = '' ) {
	if ( 'productos' === $slug ) {
		if ( function_exists( 'wc_get_page_permalink' ) ) {
			return wc_get_page_permalink( 'shop' );
		}
		return home_url( '/' );
	}
	$page = get_page_by_path( $slug );
	if ( $page ) {
		return get_permalink( $page );
	}
	return $fallback ? $fallback : home_url( '/' . $slug . '/' );
}

/** URL de un producto por su slug, o de la tienda si aún no existe. */
function maison_product_url( $slug ) {
	$post = get_page_by_path( $slug, OBJECT, 'product' );
	return $post ? get_permalink( $post ) : maison_page_url( 'productos' );
}

/** URL de la página de contacto con un asunto ya rellenado. */
function maison_contact_url( $subject = '' ) {
	$url = maison_page_url( 'contacto' );
	return $subject ? add_query_arg( 'asunto', rawurlencode( $subject ), $url ) : $url;
}

/** Enlaces de reserva cuando aún no se ha creado un menú. */
function maison_menu_fallback( $items ) {
	echo '<ul>';
	foreach ( $items as $slug => $label ) {
		printf( '<li><a href="%s">%s</a></li>', esc_url( maison_page_url( $slug ) ), esc_html( $label ) );
	}
	echo '</ul>';
}

function maison_primary_fallback() {
	$items = array(
		'inicio'         => __( 'Inicio', 'maison' ),
		'productos'      => __( 'Producto', 'maison' ),
		'sobre-nosotros' => __( 'Sobre nosotros', 'maison' ),
		'faqs'           => __( 'FAQs', 'maison' ),
		'contacto'       => __( 'Contacto', 'maison' ),
	);
	echo '<ul>';
	foreach ( $items as $slug => $label ) {
		$url = 'inicio' === $slug ? home_url( '/' ) : maison_page_url( $slug );
		printf( '<li><a href="%s">%s</a></li>', esc_url( $url ), esc_html( $label ) );
	}
	echo '</ul>';
}

function maison_footer_info_fallback() {
	maison_menu_fallback(
		array(
			'envios'       => __( 'Política de envíos y entregas', 'maison' ),
			'garantia'     => __( 'Garantía', 'maison' ),
			'devoluciones' => __( 'Política de devoluciones', 'maison' ),
			'contacto'     => __( 'Contacto', 'maison' ),
		)
	);
}

function maison_footer_house_fallback() {
	maison_menu_fallback(
		array(
			'productos'      => __( 'Equipamiento', 'maison' ),
			'sobre-nosotros' => __( 'Sobre nosotros', 'maison' ),
			'faqs'           => __( 'FAQs', 'maison' ),
			'maison-care'    => __( 'Maison Care', 'maison' ),
		)
	);
}

/** Iconos SVG en línea. */
function maison_icon( $name ) {
	$icons = array(
		'mail'  => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M4 6h16v12H4z"/><path d="m4 7 8 6 8-6"/></svg>',
		'bag'   => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M5 8h14l-1 12H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
		'phone' => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M5 3h3l2 5-2.5 1.5a11 11 0 0 0 7 7L16 14l5 2v3a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>',
	);
	return isset( $icons[ $name ] ) ? $icons[ $name ] : '';
}
