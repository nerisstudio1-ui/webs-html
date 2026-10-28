<?php
/**
 * Opciones editables desde Apariencia → Personalizar → Maison Reformer.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

/** Valores por defecto de todas las opciones del tema. */
function maison_defaults() {
	return array(
		'topbar'        => 'Bienvenida a Maison · Equipamiento de Pilates con envío gratuito a España peninsular',
		'hero_title'    => 'Madera natural. Esencia Maison.',
		'hero_subtitle' => 'Equipamiento de Pilates',
		'hero_image'    => maison_img( 'cadillac.jpg' ),
		'grid_title'    => 'Nuestra colección',
		'banner_title'  => 'Equipa tu estudio con nosotros',
		'banner_text'   => 'Te asesoramos para encontrar el equipamiento que mejor se adapta a tu espacio, con entrega interior y montaje bajo petición.',
		'banner_image'  => maison_img( 'wunda-chair.jpg' ),
		'duo1_image'    => maison_img( 'hero.jpg' ),
		'spotlight_image' => maison_img( 'the-icon.jpg' ),
		'statement'     => 'Creemos que los detalles marcan la diferencia. La elección de los materiales, los acabados y la estética de nuestros equipos merecen el mismo cuidado que la forma en que escuchamos y atendemos a quienes nos eligen.',
		'hero_lead'     => 'Reformers y equipos de Pilates en madera natural, pensados para estudios profesionales y espacios en casa.',
		'words'         => 'Madera natural · Diseño minimalista · Calidez · Funcionalidad · Serenidad',
		'split1_image'  => maison_img( 'the-maison.jpg' ),
		'mosaic1'       => maison_img( 'wall-tower.jpg' ),
		'mosaic2'       => maison_img( 'wunda-chair.jpg' ),
		'mosaic3'       => maison_img( 'ladder-barrel.jpg' ),
		'instagram_url'    => '',
		'instagram_handle' => '@maisonreformer',
		'insta1'        => maison_img( 'the-icon.jpg' ),
		'insta2'        => maison_img( 'wall-tower.jpg' ),
		'insta3'        => maison_img( 'ladder-barrel.jpg' ),
		'insta4'        => maison_img( 'wunda-chair.jpg' ),
		'email'         => 'maisonreformer@gmail.com',
		'phone'         => '+34 XXX XXX XXX',
		'whatsapp'      => '',
		'motto'         => 'Una casa para tu movimiento.',
	);
}

/** Lee una opción del tema con su valor por defecto. */
function maison_mod( $key ) {
	$defaults = maison_defaults();
	$value    = get_theme_mod( 'maison_' . $key, isset( $defaults[ $key ] ) ? $defaults[ $key ] : '' );
	return '' === $value && isset( $defaults[ $key ] ) && false !== strpos( $key, 'image' ) ? $defaults[ $key ] : $value;
}

add_action( 'customize_register', 'maison_customize_register' );
function maison_customize_register( $wp_customize ) {
	$defaults = maison_defaults();

	$wp_customize->add_panel( 'maison', array( 'title' => __( 'Maison Reformer', 'maison' ), 'priority' => 30 ) );

	$sections = array(
		'maison_general' => array(
			'title'  => __( 'Cabecera y contacto', 'maison' ),
			'fields' => array(
				'topbar'   => array( __( 'Texto de la barra superior', 'maison' ), 'text' ),
				'email'    => array( __( 'Email de contacto (recibe el formulario)', 'maison' ), 'email' ),
				'phone'    => array( __( 'Teléfono', 'maison' ), 'text' ),
				'whatsapp' => array( __( 'WhatsApp (formato 34600000000)', 'maison' ), 'text' ),
				'instagram_url'    => array( __( 'Instagram: enlace al perfil', 'maison' ), 'url' ),
				'instagram_handle' => array( __( 'Instagram: nombre (@usuario)', 'maison' ), 'text' ),
				'motto'    => array( __( 'Lema del pie', 'maison' ), 'text' ),
			),
		),
		'maison_home'    => array(
			'title'  => __( 'Página de inicio', 'maison' ),
			'fields' => array(
				'hero_title'    => array( __( 'Título principal', 'maison' ), 'text' ),
				'hero_subtitle' => array( __( 'Subtítulo', 'maison' ), 'text' ),
				'hero_image'    => array( __( 'Imagen principal', 'maison' ), 'image' ),
				'hero_lead'     => array( __( 'Texto bajo el título', 'maison' ), 'textarea' ),
				'statement'     => array( __( 'Frase "La esencia Maison"', 'maison' ), 'textarea' ),
				'grid_title'    => array( __( 'Título del carrusel de productos', 'maison' ), 'text' ),
				'duo1_image'    => array( __( '"Para tu estudio": imagen', 'maison' ), 'image' ),
				'banner_title'  => array( __( 'Banda: título', 'maison' ), 'text' ),
				'banner_text'   => array( __( 'Banda: texto', 'maison' ), 'textarea' ),
				'banner_image'  => array( __( 'Banda: imagen', 'maison' ), 'image' ),
				'split1_image'  => array( __( '"Para tu hogar": imagen', 'maison' ), 'image' ),
				'insta1'        => array( __( 'Instagram: foto 1', 'maison' ), 'image' ),
				'insta2'        => array( __( 'Instagram: foto 2', 'maison' ), 'image' ),
				'insta3'        => array( __( 'Instagram: foto 3', 'maison' ), 'image' ),
				'insta4'        => array( __( 'Instagram: foto 4', 'maison' ), 'image' ),
				'spotlight_image' => array( __( 'Producto destacado (The Icon): imagen', 'maison' ), 'image' ),
			),
		),
	);

	foreach ( $sections as $section_id => $section ) {
		$wp_customize->add_section( $section_id, array( 'title' => $section['title'], 'panel' => 'maison' ) );
		foreach ( $section['fields'] as $key => $field ) {
			list( $label, $type ) = $field;
			$sanitize = ( 'image' === $type || 'url' === $type ) ? 'esc_url_raw' : ( 'email' === $type ? 'sanitize_email' : ( 'textarea' === $type ? 'sanitize_textarea_field' : 'sanitize_text_field' ) );
			$wp_customize->add_setting(
				'maison_' . $key,
				array(
					'default'           => $defaults[ $key ],
					'sanitize_callback' => $sanitize,
				)
			);
			if ( 'image' === $type ) {
				$wp_customize->add_control(
					new WP_Customize_Image_Control( $wp_customize, 'maison_' . $key, array( 'label' => $label, 'section' => $section_id ) )
				);
			} else {
				$wp_customize->add_control( 'maison_' . $key, array( 'label' => $label, 'section' => $section_id, 'type' => $type ) );
			}
		}
	}
}
