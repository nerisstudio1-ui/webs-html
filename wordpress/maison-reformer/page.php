<?php
/**
 * Páginas: Sobre nosotros, FAQs, políticas, Maison Care…
 * Si la página tiene imagen destacada, se muestra como cabecera a sangre.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();

while ( have_posts() ) :
	the_post();
	if ( has_post_thumbnail() ) :
		?>
		<section class="page-hero">
			<?php the_post_thumbnail( 'full' ); ?>
			<h1><?php the_title(); ?></h1>
		</section>
		<div style="height:60px"></div>
	<?php else : ?>
		<section class="page-head">
			<h1><?php the_title(); ?></h1>
			<?php if ( has_excerpt() ) : ?>
				<p><?php echo esc_html( get_the_excerpt() ); ?></p>
			<?php endif; ?>
		</section>
	<?php endif; ?>
	<article class="prose">
		<?php the_content(); ?>
	</article>
	<?php
endwhile;

get_footer();
