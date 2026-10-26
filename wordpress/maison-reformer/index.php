<?php
/**
 * Plantilla de reserva (blog, archivos, búsquedas).
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<section class="page-head">
	<h1><?php echo is_home() ? esc_html( get_the_title( get_option( 'page_for_posts' ) ) ) : wp_kses_post( get_the_archive_title() ); ?></h1>
</section>
<div class="prose">
	<?php if ( have_posts() ) : ?>
		<?php
		while ( have_posts() ) :
			the_post();
			?>
			<article <?php post_class(); ?>>
				<h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
				<?php is_singular() ? the_content() : the_excerpt(); ?>
			</article>
		<?php endwhile; ?>
		<?php the_posts_pagination(); ?>
	<?php else : ?>
		<p><?php esc_html_e( 'No hay contenido todavía.', 'maison' ); ?></p>
	<?php endif; ?>
</div>
<?php
get_footer();
