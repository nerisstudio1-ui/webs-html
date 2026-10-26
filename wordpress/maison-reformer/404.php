<?php
/**
 * Página no encontrada.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<section class="page-head" style="padding-bottom:120px">
	<h1><?php esc_html_e( 'Página no encontrada', 'maison' ); ?></h1>
	<p><?php esc_html_e( 'La página que buscas no existe o ha cambiado de dirección.', 'maison' ); ?></p>
	<p style="margin-top:34px"><a class="btn" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Volver al inicio', 'maison' ); ?></a></p>
</section>
<?php
get_footer();
