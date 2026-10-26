<?php
/**
 * Página de inicio.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();

$marquee = trim( maison_mod( 'marquee' ) );
$marquee = $marquee ? str_repeat( $marquee . ' · ', 4 ) : '';
?>
<section class="hero">
	<img src="<?php echo esc_url( maison_mod( 'hero_image' ) ); ?>" alt="" fetchpriority="high">
	<div class="hero-text">
		<h1><?php echo esc_html( maison_mod( 'hero_title' ) ); ?></h1>
		<?php if ( maison_mod( 'hero_subtitle' ) ) : ?>
			<p><?php echo esc_html( maison_mod( 'hero_subtitle' ) ); ?></p>
		<?php endif; ?>
	</div>
</section>

<?php if ( $marquee ) : ?>
	<div class="marquee"><div class="marquee-track"><span><?php echo esc_html( $marquee ); ?></span><span aria-hidden="true"><?php echo esc_html( $marquee ); ?></span></div></div>
<?php endif; ?>

<section class="section">
	<div class="wrap">
		<h2 class="section-title"><?php echo esc_html( maison_mod( 'grid_title' ) ); ?></h2>
		<?php
		if ( class_exists( 'WooCommerce' ) ) {
			echo do_shortcode( '[products limit="4" columns="4" orderby="menu_order" order="ASC"]' );
		}
		?>
	</div>
</section>

<section class="banner">
	<img src="<?php echo esc_url( maison_mod( 'banner_image' ) ); ?>" alt="" loading="lazy">
	<div class="inner reveal">
		<h2 class="big-title"><?php echo esc_html( maison_mod( 'banner_title' ) ); ?></h2>
		<p><?php echo esc_html( maison_mod( 'banner_text' ) ); ?></p>
		<a class="btn btn-ghost" href="<?php echo esc_url( maison_contact_url( 'Equipar mi estudio' ) ); ?>"><?php esc_html_e( 'Hablemos de tu proyecto', 'maison' ); ?></a>
	</div>
</section>

<section class="split">
	<figure><img src="<?php echo esc_url( maison_mod( 'split1_image' ) ); ?>" alt="" loading="lazy"></figure>
	<div class="copy reveal">
		<div class="eyebrow"><?php esc_html_e( 'Reformer The Maison', 'maison' ); ?></div>
		<h2 class="big-title"><?php esc_html_e( 'Un espacio de calma en tu hogar', 'maison' ); ?></h2>
		<p><?php esc_html_e( 'Diseño plegable, estructura de madera y tapizado cálido para integrar Pilates en tu día a día sin renunciar al espacio.', 'maison' ); ?></p>
		<a class="btn btn-line" href="<?php echo esc_url( maison_page_url( 'productos' ) ); ?>"><?php esc_html_e( 'Descubrir', 'maison' ); ?></a>
	</div>
</section>

<section class="mosaic">
	<?php foreach ( array( 'mosaic1', 'mosaic2', 'mosaic3' ) as $key ) : ?>
		<figure><img src="<?php echo esc_url( maison_mod( $key ) ); ?>" alt="" loading="lazy"></figure>
	<?php endforeach; ?>
</section>

<section class="split reverse">
	<figure><img src="<?php echo esc_url( maison_mod( 'split2_image' ) ); ?>" alt="" loading="lazy"></figure>
	<div class="copy reveal">
		<div class="eyebrow"><?php esc_html_e( 'Sobre nosotros', 'maison' ); ?></div>
		<h2 class="big-title"><?php esc_html_e( 'Calidad y diseño con un propósito', 'maison' ); ?></h2>
		<p><?php esc_html_e( 'Equipamiento de Pilates que combina calidad, diseño y funcionalidad, acompañado de una atención a la altura de cada inversión.', 'maison' ); ?></p>
		<a class="btn btn-line" href="<?php echo esc_url( maison_page_url( 'sobre-nosotros' ) ); ?>"><?php esc_html_e( 'Conócenos', 'maison' ); ?></a>
	</div>
</section>

<?php
// Contenido añadido desde el editor a la página de inicio (opcional).
while ( have_posts() ) :
	the_post();
	if ( get_the_content() ) :
		?>
		<section class="prose"><?php the_content(); ?></section>
		<?php
	endif;
endwhile;
?>

<section class="cta">
	<h2 class="big-title"><?php esc_html_e( 'Hablemos de tu proyecto', 'maison' ); ?></h2>
	<p><?php esc_html_e( 'Déjanos tu email y te ayudamos a elegir tu equipo.', 'maison' ); ?></p>
	<form class="pill" action="<?php echo esc_url( maison_page_url( 'contacto' ) ); ?>" method="get">
		<input type="email" name="email" placeholder="<?php esc_attr_e( 'Dirección de correo electrónico', 'maison' ); ?>" aria-label="Email" required>
		<button type="submit" aria-label="<?php esc_attr_e( 'Enviar', 'maison' ); ?>">&rarr;</button>
	</form>
</section>
<?php
get_footer();
