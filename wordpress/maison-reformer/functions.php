<?php
/**
 * Maison Reformer — funciones del tema.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

define( 'MAISON_VERSION', '1.0.0' );
define( 'MAISON_DIR', get_template_directory() );
define( 'MAISON_URI', get_template_directory_uri() );

require MAISON_DIR . '/inc/setup.php';
require MAISON_DIR . '/inc/customizer.php';
require MAISON_DIR . '/inc/contact.php';
require MAISON_DIR . '/inc/importer.php';

if ( class_exists( 'WooCommerce' ) ) {
	require MAISON_DIR . '/inc/woocommerce.php';
}
