<?php
/**
 * Pie del sitio.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;
?>
</main>
<footer class="footer">
	<div class="footer-top">
		<div>
			<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>"><img src="<?php echo esc_url( maison_img( 'logo-light.png' ) ); ?>" alt="<?php bloginfo( 'name' ); ?>" width="160" height="45"></a>
			<p class="motto"><?php echo esc_html( maison_mod( 'motto' ) ); ?></p>
		</div>
		<div class="footer-cols">
			<div>
				<h4><?php esc_html_e( 'Información', 'maison' ); ?></h4>
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'footer_info',
						'container'      => false,
						'depth'          => 1,
						'fallback_cb'    => 'maison_footer_info_fallback',
					)
				);
				?>
			</div>
			<div>
				<h4><?php esc_html_e( 'Maison', 'maison' ); ?></h4>
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'footer_house',
						'container'      => false,
						'depth'          => 1,
						'fallback_cb'    => 'maison_footer_house_fallback',
					)
				);
				?>
			</div>
			<div>
				<h4><?php esc_html_e( 'Contacto', 'maison' ); ?></h4>
				<ul>
					<?php if ( maison_mod( 'email' ) ) : ?>
						<li><a href="mailto:<?php echo esc_attr( antispambot( maison_mod( 'email' ) ) ); ?>"><?php echo esc_html( antispambot( maison_mod( 'email' ) ) ); ?></a></li>
					<?php endif; ?>
					<?php if ( maison_mod( 'phone' ) ) : ?>
						<li><a href="tel:<?php echo esc_attr( preg_replace( '/[^0-9+]/', '', maison_mod( 'phone' ) ) ); ?>"><?php echo esc_html( maison_mod( 'phone' ) ); ?></a></li>
					<?php endif; ?>
				</ul>
			</div>
		</div>
	</div>
	<div class="footer-bottom">
		<span>&copy; <?php echo esc_html( wp_date( 'Y' ) ); ?> <?php bloginfo( 'name' ); ?></span>
		<span>
			<a href="<?php echo esc_url( get_privacy_policy_url() ? get_privacy_policy_url() : maison_page_url( 'privacidad' ) ); ?>"><?php esc_html_e( 'Política de privacidad', 'maison' ); ?></a>
			<a href="<?php echo esc_url( maison_page_url( 'envios' ) ); ?>"><?php esc_html_e( 'Envíos', 'maison' ); ?></a>
			<a href="<?php echo esc_url( maison_page_url( 'devoluciones' ) ); ?>"><?php esc_html_e( 'Devoluciones', 'maison' ); ?></a>
		</span>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
