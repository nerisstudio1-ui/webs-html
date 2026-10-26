<?php
/**
 * Envoltorio de las páginas de WooCommerce (tienda, categorías y ficha de producto).
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();

if ( is_product() ) :
	woocommerce_content();
else :
	$current = is_product_category() ? get_queried_object_id() : 0;
	$terms   = get_terms(
		array(
			'taxonomy'   => 'product_cat',
			'hide_empty' => true,
			'exclude'    => array( (int) get_option( 'default_product_cat' ) ),
		)
	);
	?>
	<section class="page-head">
		<h1><?php woocommerce_page_title(); ?></h1>
		<?php if ( ! is_product_category() || ! term_description() ) : ?>
			<p><?php esc_html_e( 'Piezas de madera natural para estudios de Pilates y espacios en casa.', 'maison' ); ?></p>
		<?php else : ?>
			<?php echo wp_kses_post( term_description() ); ?>
		<?php endif; ?>
	</section>
	<div class="wrap shop-wrap">
		<?php if ( ! is_wp_error( $terms ) && $terms ) : ?>
			<nav class="filters" aria-label="<?php esc_attr_e( 'Categorías', 'maison' ); ?>">
				<a href="<?php echo esc_url( wc_get_page_permalink( 'shop' ) ); ?>"<?php echo $current ? '' : ' class="active"'; ?>><?php esc_html_e( 'Todo', 'maison' ); ?></a>
				<?php foreach ( $terms as $term ) : ?>
					<a href="<?php echo esc_url( get_term_link( $term ) ); ?>"<?php echo $current === $term->term_id ? ' class="active"' : ''; ?>><?php echo esc_html( $term->name ); ?></a>
				<?php endforeach; ?>
			</nav>
		<?php endif; ?>
		<?php woocommerce_content(); ?>
	</div>
	<?php
endif;

get_footer();
