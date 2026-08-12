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
 * ---------------------------------------------------------------------------
 * Tipografias propias
 * ---------------------------------------------------------------------------
 *
 * El subidor de fuentes de Elementor es de pago, asi que aqui se resuelve a
 * mano: se declaran las fuentes de assets/fonts/ con @font-face y ademas se
 * anaden al desplegable de tipografias de Elementor, para que se puedan elegir
 * desde el editor como cualquier otra.
 *
 * Para anadir una fuente, basta con dejar el archivo en assets/fonts/ con este
 * nombre:
 *
 *     familia-peso-estilo.woff2
 *     blomstra-display-400-normal.woff2   ->  "Blomstra Display", 400, normal
 *     blomstra-display-700-italic.woff2   ->  "Blomstra Display", 700, italica
 *
 * No hay que tocar codigo: se detectan solas.
 */

/**
 * Lee assets/fonts/ y devuelve las fuentes encontradas agrupadas por familia.
 *
 * @return array<string, array<int, array{url:string,weight:string,style:string}>>
 */
function blomstra_child_get_custom_fonts() {
	static $fonts = null;

	if ( null !== $fonts ) {
		return $fonts;
	}

	$fonts = array();
	$dir   = get_stylesheet_directory() . '/assets/fonts';

	if ( ! is_dir( $dir ) ) {
		return $fonts;
	}

	foreach ( (array) glob( $dir . '/*.{woff2,woff,ttf}', GLOB_BRACE ) as $path ) {
		$name = pathinfo( $path, PATHINFO_FILENAME );

		// familia-peso-estilo: el peso y el estilo son los dos ultimos trozos.
		if ( ! preg_match( '/^(.+)-(\d{3})-(normal|italic)$/', $name, $m ) ) {
			continue;
		}

		$family = ucwords( str_replace( '-', ' ', $m[1] ) );

		$fonts[ $family ][] = array(
			'url'    => get_stylesheet_directory_uri() . '/assets/fonts/' . basename( $path ),
			'weight' => $m[2],
			'style'  => $m[3],
		);
	}

	return $fonts;
}

/**
 * Genera las reglas @font-face de las fuentes encontradas.
 */
function blomstra_child_font_face_css() {
	$css = '';

	foreach ( blomstra_child_get_custom_fonts() as $family => $faces ) {
		foreach ( $faces as $face ) {
			$ext    = pathinfo( $face['url'], PATHINFO_EXTENSION );
			$format = 'ttf' === $ext ? 'truetype' : $ext;

			$css .= sprintf(
				'@font-face{font-family:"%1$s";font-style:%2$s;font-weight:%3$s;font-display:swap;src:url("%4$s") format("%5$s");}',
				$family,
				$face['style'],
				$face['weight'],
				esc_url( $face['url'] ),
				$format
			);
		}
	}

	return $css;
}

/**
 * Inyecta las @font-face en la web y tambien dentro del editor de Elementor,
 * para que al maquetar se vea la tipografia real.
 */
function blomstra_child_enqueue_custom_fonts() {
	$css = blomstra_child_font_face_css();

	if ( '' === $css ) {
		return;
	}

	wp_register_style( 'blomstra-fonts', false, array(), BLOMSTRA_CHILD_VERSION );
	wp_enqueue_style( 'blomstra-fonts' );
	wp_add_inline_style( 'blomstra-fonts', $css );
}
add_action( 'wp_enqueue_scripts', 'blomstra_child_enqueue_custom_fonts', 5 );
add_action( 'elementor/editor/after_enqueue_styles', 'blomstra_child_enqueue_custom_fonts' );
add_action( 'elementor/preview/enqueue_styles', 'blomstra_child_enqueue_custom_fonts' );

/**
 * Anade un grupo "Blomstra" al selector de tipografias de Elementor.
 *
 * @param array $groups Grupos existentes.
 * @return array
 */
function blomstra_child_elementor_font_group( $groups ) {
	if ( blomstra_child_get_custom_fonts() ) {
		$groups['blomstra'] = __( 'Blomstra', 'blomstra-child' );
	}

	return $groups;
}
add_filter( 'elementor/fonts/groups', 'blomstra_child_elementor_font_group' );

/**
 * Mete las fuentes propias en ese grupo, para poder elegirlas en el editor.
 *
 * @param array $fonts Fuentes existentes.
 * @return array
 */
function blomstra_child_elementor_fonts( $fonts ) {
	foreach ( array_keys( blomstra_child_get_custom_fonts() ) as $family ) {
		$fonts[ $family ] = 'blomstra';
	}

	return $fonts;
}
add_filter( 'elementor/fonts/additional_fonts', 'blomstra_child_elementor_fonts' );

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
