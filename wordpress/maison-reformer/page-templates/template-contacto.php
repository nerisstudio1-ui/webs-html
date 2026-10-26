<?php
/**
 * Template Name: Contacto
 *
 * Formulario "Hablemos de tu proyecto" con teléfono y email.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();

// phpcs:disable WordPress.Security.NonceVerification.Recommended -- solo se leen valores para rellenar el formulario.
$subject = isset( $_GET['asunto'] ) ? sanitize_text_field( wp_unslash( $_GET['asunto'] ) ) : '';
$email   = isset( $_GET['email'] ) ? sanitize_email( wp_unslash( $_GET['email'] ) ) : '';
$sent    = isset( $_GET['enviado'] );
$error   = isset( $_GET['error'] );
// phpcs:enable
$privacy = get_privacy_policy_url() ? get_privacy_policy_url() : maison_page_url( 'privacidad' );
?>
<section class="page-head">
	<div class="eyebrow"><?php esc_html_e( 'Estamos para ayudarte', 'maison' ); ?></div>
	<h1><?php esc_html_e( 'Hablemos de tu proyecto.', 'maison' ); ?></h1>
	<p><?php esc_html_e( 'Cuéntanos qué necesitas y te ayudaremos a encontrar el equipamiento para tu espacio.', 'maison' ); ?></p>
</section>

<section class="contact">
	<?php if ( $sent ) : ?>
		<p class="notice"><?php esc_html_e( 'Gracias por escribirnos. Te responderemos lo antes posible.', 'maison' ); ?></p>
	<?php elseif ( $error ) : ?>
		<p class="notice notice-error"><?php esc_html_e( 'No hemos podido enviar el mensaje. Revisa los campos obligatorios o escríbenos directamente por email.', 'maison' ); ?></p>
	<?php endif; ?>

	<form class="form" method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
		<input type="hidden" name="action" value="maison_contact">
		<?php wp_nonce_field( 'maison_contact', 'maison_nonce' ); ?>
		<div class="hp" aria-hidden="true"><label>Web <input type="text" name="web" tabindex="-1" autocomplete="off"></label></div>
		<div><label for="nombre"><?php esc_html_e( 'Nombre *', 'maison' ); ?></label><input type="text" id="nombre" name="nombre" autocomplete="given-name" required></div>
		<div><label for="apellidos"><?php esc_html_e( 'Apellidos *', 'maison' ); ?></label><input type="text" id="apellidos" name="apellidos" autocomplete="family-name" required></div>
		<div><label for="email"><?php esc_html_e( 'Email *', 'maison' ); ?></label><input type="email" id="email" name="email" autocomplete="email" value="<?php echo esc_attr( $email ); ?>" required></div>
		<div><label for="telefono"><?php esc_html_e( 'Teléfono', 'maison' ); ?></label><input type="tel" id="telefono" name="telefono" autocomplete="tel"></div>
		<div class="full"><label for="asunto"><?php esc_html_e( 'Asunto *', 'maison' ); ?></label><input type="text" id="asunto" name="asunto" value="<?php echo esc_attr( $subject ); ?>" required></div>
		<div class="full"><label for="mensaje"><?php esc_html_e( 'Mensaje *', 'maison' ); ?></label><textarea id="mensaje" name="mensaje" placeholder="<?php esc_attr_e( 'Cuéntanos cómo podemos ayudarte…', 'maison' ); ?>" required></textarea></div>
		<label class="check full"><input type="checkbox" name="privacidad" value="1" required> <span><?php printf( wp_kses_post( __( 'He leído y acepto la <a href="%s">política de privacidad</a>.', 'maison' ) ), esc_url( $privacy ) ); ?></span></label>
		<p class="req full"><?php esc_html_e( '* Campos obligatorios', 'maison' ); ?></p>
		<div class="full"><button type="submit" class="btn btn-block"><?php esc_html_e( 'Enviar mensaje', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></button></div>
	</form>

	<div class="contact-data">
		<div>
			<?php echo maison_icon( 'phone' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
			<div class="eyebrow"><?php esc_html_e( 'Teléfono', 'maison' ); ?></div>
			<a href="tel:<?php echo esc_attr( preg_replace( '/[^0-9+]/', '', maison_mod( 'phone' ) ) ); ?>"><?php echo esc_html( maison_mod( 'phone' ) ); ?></a>
		</div>
		<div>
			<?php echo maison_icon( 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
			<div class="eyebrow"><?php esc_html_e( 'Email', 'maison' ); ?></div>
			<a href="mailto:<?php echo esc_attr( antispambot( maison_mod( 'email' ) ) ); ?>"><?php echo esc_html( antispambot( maison_mod( 'email' ) ) ); ?></a>
		</div>
	</div>

	<?php
	while ( have_posts() ) :
		the_post();
		if ( get_the_content() ) :
			?>
			<div class="prose" style="padding-top:50px"><?php the_content(); ?></div>
			<?php
		endif;
	endwhile;
	?>
</section>
<?php
get_footer();
