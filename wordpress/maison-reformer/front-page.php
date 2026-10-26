<?php
/**
 * Página de inicio.
 *
 * @package MaisonReformer
 */

defined( 'ABSPATH' ) || exit;

get_header();

$products = class_exists( 'WooCommerce' ) ? wc_get_products(
	array(
		'status'  => 'publish',
		'limit'   => 12,
		'orderby' => 'menu_order',
		'order'   => 'ASC',
	)
) : array();
?>
<section class="hero">
	<img class="hero-img" src="<?php echo esc_url( maison_mod( 'hero_image' ) ); ?>" alt="" fetchpriority="high">
	<div class="hero-text">
		<div class="hero-inner">
			<?php if ( maison_mod( 'hero_subtitle' ) ) : ?>
				<p class="hero-eyebrow"><?php echo esc_html( maison_mod( 'hero_subtitle' ) ); ?></p>
			<?php endif; ?>
			<h1>
				<?php
				// La segunda frase del título se muestra en cursiva.
				$parts = preg_split( '/(?<=\.)\s+/', maison_mod( 'hero_title' ), 2 );
				echo esc_html( $parts[0] );
				if ( isset( $parts[1] ) ) {
					echo '<br><em>' . esc_html( $parts[1] ) . '</em>';
				}
				?>
			</h1>
			<p class="hero-lead"><?php echo esc_html( maison_mod( 'hero_lead' ) ); ?></p>
			<div class="hero-actions">
				<a class="btn btn-light" href="<?php echo esc_url( maison_page_url( 'productos' ) ); ?>"><?php esc_html_e( 'Descubrir la colección', 'maison' ); ?></a>
			</div>
		</div>
	</div>
	<a class="scroll-cue" href="#ventajas" aria-label="<?php esc_attr_e( 'Bajar', 'maison' ); ?>"><span></span></a>
</section>

<section class="perks" id="ventajas">
	<div class="perk reveal">
		<h3><?php esc_html_e( 'Envío gratuito', 'maison' ); ?></h3>
		<p><?php esc_html_e( 'A toda España peninsular', 'maison' ); ?></p>
	</div>
	<div class="perk reveal" style="--d:.1s">
		<h3><?php esc_html_e( 'Entrega en 24/48 h', 'maison' ); ?></h3>
		<p><?php esc_html_e( 'Laborables, productos en stock', 'maison' ); ?></p>
	</div>
	<div class="perk reveal" style="--d:.2s">
		<h3><?php esc_html_e( '3 años de garantía', 'maison' ); ?></h3>
		<p><?php esc_html_e( 'Garantía legal para particulares', 'maison' ); ?></p>
	</div>
	<div class="perk reveal" style="--d:.3s">
		<h3><?php esc_html_e( 'Asesoramiento', 'maison' ); ?></h3>
		<p><?php esc_html_e( 'Personalizado, antes y después', 'maison' ); ?></p>
	</div>
</section>

<section class="statement">
	<div class="narrow reveal">
		<p class="eyebrow"><?php esc_html_e( 'La esencia Maison', 'maison' ); ?></p>
		<p class="statement-text"><?php echo esc_html( maison_mod( 'statement' ) ); ?></p>
		<a class="link-arrow" href="<?php echo esc_url( maison_page_url( 'sobre-nosotros' ) ); ?>"><?php esc_html_e( 'Conoce Maison', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></a>
	</div>
</section>

<?php if ( $products ) : ?>
	<section class="collection">
		<div class="wrap">
			<div class="collection-head">
				<h2 class="big-title"><?php echo esc_html( maison_mod( 'grid_title' ) ); ?></h2>
				<div class="carousel-nav">
					<a class="link-arrow" href="<?php echo esc_url( maison_page_url( 'productos' ) ); ?>"><?php esc_html_e( 'Ver todo', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></a>
					<button type="button" class="round" data-carousel-prev aria-label="<?php esc_attr_e( 'Anterior', 'maison' ); ?>">&larr;</button>
					<button type="button" class="round" data-carousel-next aria-label="<?php esc_attr_e( 'Siguiente', 'maison' ); ?>">&rarr;</button>
				</div>
			</div>
		</div>
		<div class="carousel" data-carousel>
			<?php
			foreach ( $products as $product ) :
				$terms = get_the_terms( $product->get_id(), 'product_cat' );
				?>
				<a class="card" href="<?php echo esc_url( $product->get_permalink() ); ?>">
					<figure><?php echo $product->get_image( 'woocommerce_thumbnail', array( 'loading' => 'lazy' ) ); // phpcs:ignore WordPress.Security.EscapeOutput ?></figure>
					<div class="meta">
						<div class="name"><?php echo esc_html( $product->get_name() ); ?></div>
						<?php if ( $terms && ! is_wp_error( $terms ) ) : ?>
							<div><?php echo esc_html( $terms[0]->name ); ?></div>
						<?php endif; ?>
						<div><?php echo wp_kses_post( $product->get_price_html() ); ?></div>
					</div>
				</a>
			<?php endforeach; ?>
		</div>
	</section>
<?php endif; ?>

<section class="duo">
	<a class="duo-tile reveal" href="<?php echo esc_url( maison_contact_url( 'Equipar mi estudio' ) ); ?>">
		<img src="<?php echo esc_url( maison_mod( 'duo1_image' ) ); ?>" alt="" loading="lazy">
		<div class="duo-text">
			<span class="eyebrow"><?php esc_html_e( 'Profesionales', 'maison' ); ?></span>
			<h3><?php esc_html_e( 'Para tu estudio', 'maison' ); ?></h3>
			<span class="link-arrow"><?php esc_html_e( 'Equipa tu centro', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></span>
		</div>
	</a>
	<a class="duo-tile reveal" style="--d:.15s" href="<?php echo esc_url( maison_product_url( 'the-maison' ) ); ?>">
		<img src="<?php echo esc_url( maison_mod( 'split1_image' ) ); ?>" alt="" loading="lazy">
		<div class="duo-text">
			<span class="eyebrow"><?php esc_html_e( 'Particulares', 'maison' ); ?></span>
			<h3><?php esc_html_e( 'Para tu hogar', 'maison' ); ?></h3>
			<span class="link-arrow"><?php esc_html_e( 'Descubre The Maison', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></span>
		</div>
	</a>
</section>

<section class="spotlight">
	<figure class="spotlight-img reveal"><img src="<?php echo esc_url( maison_mod( 'spotlight_image' ) ); ?>" alt="" loading="lazy"></figure>
	<div class="spotlight-copy reveal" style="--d:.15s">
		<p class="eyebrow"><?php esc_html_e( 'Nuestro Reformer de referencia', 'maison' ); ?></p>
		<h2 class="big-title">The Icon</h2>
		<p><?php esc_html_e( 'Una pieza que representa la esencia de Maison, donde el diseño minimalista y la funcionalidad se encuentran. La torre amplía las posibilidades de práctica y se entrega con un equipamiento completo de accesorios.', 'maison' ); ?></p>
		<ul class="specs">
			<?php foreach ( array( 'Tabla de pies', 'Tabla de salto', 'Antideslizante', 'Caja box', 'Tabla mat', 'Muelles', 'Hombreras', 'Torre y cuerdas' ) as $tag ) : ?>
				<li><?php echo esc_html( $tag ); ?></li>
			<?php endforeach; ?>
		</ul>
		<a class="btn" href="<?php echo esc_url( maison_product_url( 'the-icon' ) ); ?>"><?php esc_html_e( 'Ver The Icon', 'maison' ); ?></a>
	</div>
</section>

<section class="banner parallax">
	<img src="<?php echo esc_url( maison_mod( 'banner_image' ) ); ?>" alt="" loading="lazy" data-parallax>
	<div class="inner reveal">
		<p class="eyebrow"><?php esc_html_e( 'Te acompañamos', 'maison' ); ?></p>
		<h2 class="big-title"><?php echo esc_html( maison_mod( 'banner_title' ) ); ?></h2>
		<p><?php echo esc_html( maison_mod( 'banner_text' ) ); ?></p>
		<a class="btn btn-light" href="<?php echo esc_url( maison_contact_url( 'Equipar mi estudio' ) ); ?>"><?php esc_html_e( 'Hablemos de tu proyecto', 'maison' ); ?></a>
	</div>
</section>

<section class="faq-teaser">
	<div class="wrap faq-grid">
		<div class="reveal">
			<p class="eyebrow"><?php esc_html_e( 'Resolvemos tus dudas', 'maison' ); ?></p>
			<h2 class="big-title"><?php esc_html_e( 'Preguntas frecuentes', 'maison' ); ?></h2>
			<a class="link-arrow" href="<?php echo esc_url( maison_page_url( 'faqs' ) ); ?>"><?php esc_html_e( 'Ver todas', 'maison' ); ?> <span aria-hidden="true">&rarr;</span></a>
		</div>
		<div class="faq-list reveal" style="--d:.15s">
			<details><summary><?php esc_html_e( '¿El envío es gratuito?', 'maison' ); ?></summary><p><?php esc_html_e( 'Sí, el envío estándar es gratuito en España peninsular. Para otros destinos, consúltanos las condiciones y el coste.', 'maison' ); ?></p></details>
			<details><summary><?php esc_html_e( '¿El Reformer viene montado?', 'maison' ); ?></summary><p><?php esc_html_e( 'La estructura principal viene premontada. Solo tendrás que instalar los accesorios correspondientes. Se incluyen las herramientas y las instrucciones de montaje.', 'maison' ); ?></p></details>
			<details><summary><?php esc_html_e( '¿Ofrecéis entrega en el interior y montaje?', 'maison' ); ?></summary><p><?php esc_html_e( 'Sí, podemos organizar ambos servicios previo acuerdo con nosotros. Sus condiciones y coste se concretan antes de contratarlo.', 'maison' ); ?></p></details>
			<details><summary><?php esc_html_e( '¿Qué formas de pago aceptáis?', 'maison' ); ?></summary><p><?php esc_html_e( 'Puedes pagar con tarjeta de débito, tarjeta de crédito o transferencia bancaria.', 'maison' ); ?></p></details>
		</div>
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

<?php
$insta_url = maison_mod( 'instagram_url' ) ? maison_mod( 'instagram_url' ) : 'https://www.instagram.com/';
?>
<section class="insta">
	<div class="insta-head">
		<p class="insta-title"><?php esc_html_e( 'Síguenos en Instagram', 'maison' ); ?></p>
		<a class="insta-handle" href="<?php echo esc_url( $insta_url ); ?>" target="_blank" rel="noopener"><?php echo esc_html( maison_mod( 'instagram_handle' ) ); ?></a>
	</div>
	<div class="insta-grid">
		<?php foreach ( array( 'insta1', 'insta2', 'insta3', 'insta4' ) as $i => $key ) : ?>
			<a class="reveal" style="--d:<?php echo esc_attr( $i / 10 ); ?>s" href="<?php echo esc_url( $insta_url ); ?>" target="_blank" rel="noopener"><img src="<?php echo esc_url( maison_mod( $key ) ); ?>" alt="" loading="lazy"></a>
		<?php endforeach; ?>
	</div>
</section>

<section class="cta">
	<h2 class="big-title reveal"><?php esc_html_e( 'Hablemos de tu proyecto', 'maison' ); ?></h2>
	<p><?php esc_html_e( 'Déjanos tu email y te ayudamos a elegir tu equipo.', 'maison' ); ?></p>
	<form class="pill" action="<?php echo esc_url( maison_page_url( 'contacto' ) ); ?>" method="get">
		<input type="email" name="email" placeholder="<?php esc_attr_e( 'Dirección de correo electrónico', 'maison' ); ?>" aria-label="Email" required>
		<button type="submit" aria-label="<?php esc_attr_e( 'Enviar', 'maison' ); ?>">&rarr;</button>
	</form>
</section>
<?php
get_footer();
