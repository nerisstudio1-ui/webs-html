<?php
/**
 * Formulario de contacto: envía el mensaje por email con wp_mail().
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

add_action( 'admin_post_nopriv_maison_contact', 'maison_handle_contact' );
add_action( 'admin_post_maison_contact', 'maison_handle_contact' );
function maison_handle_contact() {
	$back = wp_get_referer() ? wp_get_referer() : maison_page_url( 'contacto' );
	$back = remove_query_arg( array( 'enviado', 'error' ), $back );

	if ( ! isset( $_POST['maison_nonce'] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['maison_nonce'] ) ), 'maison_contact' ) ) {
		wp_safe_redirect( add_query_arg( 'error', '1', $back ) );
		exit;
	}

	// Campo trampa para bots: si viene relleno, se descarta en silencio.
	if ( ! empty( $_POST['web'] ) ) {
		wp_safe_redirect( add_query_arg( 'enviado', '1', $back ) );
		exit;
	}

	$data = array();
	foreach ( array( 'nombre', 'apellidos', 'email', 'telefono', 'asunto' ) as $field ) {
		$data[ $field ] = isset( $_POST[ $field ] ) ? sanitize_text_field( wp_unslash( $_POST[ $field ] ) ) : '';
	}
	$data['mensaje'] = isset( $_POST['mensaje'] ) ? sanitize_textarea_field( wp_unslash( $_POST['mensaje'] ) ) : '';

	if ( ! $data['nombre'] || ! $data['apellidos'] || ! is_email( $data['email'] ) || ! $data['asunto'] || ! $data['mensaje'] || empty( $_POST['privacidad'] ) ) {
		wp_safe_redirect( add_query_arg( 'error', '1', $back ) );
		exit;
	}

	$to   = maison_mod( 'email' ) ? maison_mod( 'email' ) : get_option( 'admin_email' );
	$body = sprintf(
		"Nombre: %s %s\nEmail: %s\nTeléfono: %s\nAsunto: %s\n\n%s",
		$data['nombre'],
		$data['apellidos'],
		$data['email'],
		$data['telefono'] ? $data['telefono'] : '—',
		$data['asunto'],
		$data['mensaje']
	);
	$sent = wp_mail(
		$to,
		'[Web Maison Reformer] ' . $data['asunto'],
		$body,
		array( 'Reply-To: ' . $data['nombre'] . ' <' . $data['email'] . '>' )
	);

	wp_safe_redirect( add_query_arg( $sent ? 'enviado' : 'error', '1', $back ) );
	exit;
}
