<?php
/**
 * Blomstra Child - funciones del tema.
 *
 * @package blomstra-child
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'BLOMSTRA_CHILD_VERSION', '1.0.0' );

/**
 * Carga la hoja del tema hijo y, despues, la hoja del diseno.
 *
 * blomstra.css es el mismo archivo que usan los prototipos de /prototype. Ahi
 * vive todo el diseno; Elementor solo aporta la estructura y las clases CSS.
 * Se versiona con filemtime para que el navegador no sirva una cache vieja
 * mientras se esta maquetando.
 */
function blomstra_child_enqueue_styles() {
	wp_enqueue_style(
		'hello-elementor-child',
		get_stylesheet_directory_uri() . '/style.css',
		array( 'hello-elementor', 'hello-elementor-theme-style' ),
		BLOMSTRA_CHILD_VERSION
	);

	$design_path = get_stylesheet_directory() . '/assets/css/blomstra.css';

	wp_enqueue_style(
		'blomstra-design',
		get_stylesheet_directory_uri() . '/assets/css/blomstra.css',
		array( 'hello-elementor-child' ),
		file_exists( $design_path ) ? (string) filemtime( $design_path ) : BLOMSTRA_CHILD_VERSION
	);
}
add_action( 'wp_enqueue_scripts', 'blomstra_child_enqueue_styles', 20 );

/**
 * Carga la hoja del diseno tambien dentro del editor de Elementor, para que lo
 * que se ve al maquetar coincida con el resultado final.
 */
function blomstra_child_enqueue_editor_styles() {
	wp_enqueue_style(
		'blomstra-design',
		get_stylesheet_directory_uri() . '/assets/css/blomstra.css',
		array(),
		BLOMSTRA_CHILD_VERSION
	);
}
add_action( 'elementor/editor/after_enqueue_styles', 'blomstra_child_enqueue_editor_styles' );
add_action( 'elementor/preview/enqueue_styles', 'blomstra_child_enqueue_editor_styles' );

/**
 * Soportes de tema.
 *
 * 'header-footer-elementor' le dice al plugin Elementor Header & Footer Builder
 * que puede sustituir el header y el footer de este tema. Es lo que usamos en
 * lugar del Theme Builder, porque el proyecto va con Elementor gratuito.
 */
function blomstra_child_setup() {
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'title-tag' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_theme_support( 'custom-logo' );
	add_theme_support( 'header-footer-elementor' );
}
add_action( 'after_setup_theme', 'blomstra_child_setup' );

/**
 * Registra los menus que usara el header construido en Elementor.
 */
function blomstra_child_register_menus() {
	register_nav_menus(
		array(
			'main'   => __( 'Menu principal', 'blomstra-child' ),
			'footer' => __( 'Menu del pie', 'blomstra-child' ),
		)
	);
}
add_action( 'init', 'blomstra_child_register_menus' );

/**
 * Enlace "saltar al contenido" para accesibilidad.
 */
function blomstra_child_skip_link() {
	printf(
		'<a class="skip-link screen-reader-text" href="#content">%s</a>',
		esc_html__( 'Saltar al contenido', 'blomstra-child' )
	);
}
add_action( 'wp_body_open', 'blomstra_child_skip_link' );
