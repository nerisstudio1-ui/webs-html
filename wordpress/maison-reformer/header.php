<?php
/**
 * Cabecera del sitio.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php if ( maison_mod( 'topbar' ) ) : ?>
	<div class="topbar"><?php echo esc_html( maison_mod( 'topbar' ) ); ?></div>
<?php endif; ?>
<header class="header">
	<div class="wrap">
		<div class="header-left">
			<button class="menu-toggle" aria-label="<?php esc_attr_e( 'Abrir menú', 'maison' ); ?>" aria-expanded="false"><span></span></button>
			<nav class="nav" aria-label="<?php esc_attr_e( 'Principal', 'maison' ); ?>">
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'primary',
						'container'      => false,
						'depth'          => 1,
						'fallback_cb'    => 'maison_primary_fallback',
					)
				);
				?>
			</nav>
		</div>
		<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home">
			<img class="logo-dark" src="<?php echo esc_url( maison_img( 'logo.png' ) ); ?>" alt="<?php bloginfo( 'name' ); ?>" width="150" height="42">
			<img class="logo-light" src="<?php echo esc_url( maison_img( 'logo-light.png' ) ); ?>" alt="" width="150" height="42">
		</a>
		<div class="header-tools">
			<a href="<?php echo esc_url( maison_page_url( 'contacto' ) ); ?>" aria-label="<?php esc_attr_e( 'Contacto', 'maison' ); ?>"><?php echo maison_icon( 'mail' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></a>
			<?php if ( function_exists( 'wc_get_cart_url' ) ) : ?>
				<a class="keep cart-link" href="<?php echo esc_url( wc_get_cart_url() ); ?>" aria-label="<?php esc_attr_e( 'Carrito', 'maison' ); ?>">
					<?php echo maison_icon( 'bag' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
					<span class="cart-count" data-cart-count><?php echo WC()->cart && WC()->cart->get_cart_contents_count() ? esc_html( WC()->cart->get_cart_contents_count() ) : ''; ?></span>
				</a>
			<?php else : ?>
				<a class="keep" href="<?php echo esc_url( maison_page_url( 'productos' ) ); ?>" aria-label="<?php esc_attr_e( 'Equipamiento', 'maison' ); ?>"><?php echo maison_icon( 'bag' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></a>
			<?php endif; ?>
		</div>
	</div>
</header>
<main id="contenido">
