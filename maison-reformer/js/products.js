/* Catálogo de Maison Reformer.
   Para añadir o editar un producto basta con modificar este listado. */
window.MAISON_CATEGORIES = [
  { id: "reformers", name: "Reformers" },
  { id: "reformers-torre", name: "Reformers con torre" },
  { id: "cadillacs", name: "Cadillacs" },
  { id: "wunda-chair", name: "Wunda Chair" },
  { id: "barrel-spine", name: "Barrel y Spine" },
  { id: "wall-tower", name: "Wall Tower" }
];

var UPHOLSTERY = ["Negro", "Gris", "Mocca"];

window.MAISON_PRODUCTS = [
  {
    id: "the-icon",
    name: "The Icon",
    fullName: "Reformer The Icon",
    category: "reformers-torre",
    image: "img/the-icon.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Mocca",
    description: [
      "Nuestro Reformer de referencia: una pieza que representa la esencia de Maison, donde el diseño minimalista y la funcionalidad se encuentran.",
      "Su estructura de madera en acabado natural aporta calidez y serenidad, tanto en un estudio de Pilates como en un espacio de entrenamiento en casa. La torre amplía las posibilidades de práctica, combinando la versatilidad del equipo con una estética cuidada.",
      "Un esencial para tu estudio. Un espacio de calma en tu hogar.",
      "El Reformer se entrega con un equipamiento completo de accesorios: tabla de pies, tabla de salto, antideslizante, caja box, tabla mat, muelles, hombreras, torre y cuerdas. Esta configuración permite adaptar el equipo a distintas modalidades de ejercicio y necesidades de entrenamiento.",
      "La estructura principal se suministra premontada, facilitando su preparación inicial. Solo es necesario instalar los accesorios correspondientes a la configuración de uso elegida."
    ],
    accessories: ["Tabla de pies", "Tabla de salto", "Antideslizante", "Caja box", "Tabla mat", "Muelles", "Hombreras", "Torre y cuerdas"]
  },
  {
    id: "the-maison",
    name: "The Maison",
    fullName: "Reformer The Maison",
    category: "reformers",
    image: "img/the-maison.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Mocca",
    description: [
      "El Reformer plegable Maison Reformer combina diseño, comodidad y funcionalidad para integrar Pilates en tu día a día. Su estructura de madera y su tapizado aportan calidez y elegancia, creando un espacio que invita a dedicarte tiempo.",
      "Práctico y fácil de usar, cuenta con una barra de pies ajustable y un sistema de cuerdas con poleas que permiten adaptar cada sesión y trabajar fuerza, movilidad y control corporal. Su diseño plegable facilita el almacenamiento al terminar, una solución para quienes desean aprovechar mejor el espacio sin renunciar a su práctica."
    ]
  },
  {
    id: "the-cadillac",
    name: "The Cadillac",
    fullName: "Reformer The Cadillac",
    category: "cadillacs",
    image: "img/cadillac.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Mocca",
    description: [
      "El Reformer Cadillac de Maison Reformer es ideal para quienes buscan un entrenamiento completo y versátil en un solo equipo. Combina las funciones del Reformer con una estructura de Cadillac e incorpora una amplia variedad de accesorios, como muelles, barras, cuerdas, agarres y elementos de suspensión.",
      "Esta configuración permite trabajar fuerza, movilidad, flexibilidad y control corporal en distintas posiciones, adaptando cada sesión a los objetivos de entrenamiento. Una opción completa para ampliar las posibilidades de tu estudio de Pilates."
    ],
    accessories: ["Muelles", "Barras", "Cuerdas", "Agarres", "Elementos de suspensión"]
  },
  {
    id: "wunda-chair",
    name: "Wunda Chair",
    fullName: "Wunda Chair",
    category: "wunda-chair",
    image: "img/wunda-chair.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Mocca",
    description: [
      "La Wunda Chair de Maison Reformer es un equipo compacto y versátil que permite trabajar fuerza, equilibrio y control corporal mediante ejercicios de Pilates en distintas posiciones.",
      "Incorpora asiento acolchado, pedal dividido con resistencia mediante muelles y asas laterales regulables que ofrecen apoyo durante la práctica. Su formato permite ampliar las opciones de entrenamiento sin ocupar el espacio de un Reformer.",
      "La estructura de madera y sus líneas minimalistas aportan calidez y armonía, integrándose tanto en estudios de Pilates como en espacios de entrenamiento en casa."
    ]
  },
  {
    id: "ladder-barrel",
    name: "Ladder Barrel",
    fullName: "Ladder Barrel",
    category: "barrel-spine",
    image: "img/ladder-barrel.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Negro",
    description: [
      "El Ladder Barrel de Maison Reformer combina un barril acolchado de superficie curva con una escalera de distintos niveles de apoyo para trabajar movilidad, flexibilidad, fuerza y control corporal.",
      "Su sistema de ajuste permite regular la distancia entre el barril y la escalera para adaptar la posición a cada ejercicio. Los apoyos inferiores acolchados amplían las opciones de colocación.",
      "Su estructura de madera y sus líneas sencillas aportan calidez y una estética cuidada, integrándose tanto en estudios de Pilates como en espacios de entrenamiento en casa."
    ]
  },
  {
    id: "spine-corrector",
    name: "Spine Corrector",
    fullName: "Spine Corrector",
    category: "barrel-spine",
    image: "img/spine-corrector.jpg",
    price: null,
    colors: UPHOLSTERY,
    defaultColor: "Negro",
    description: [
      "Un complemento versátil para enriquecer tu práctica de Pilates. Su superficie curva permite trabajar la movilidad de la columna, la apertura del pecho y la fuerza abdominal, acompañando ejercicios de flexión, extensión y estiramiento.",
      "Combina una estructura de madera de acabado natural con tapizado negro acolchado y una barra transversal de apoyo. Su diseño compacto y elegante se integra fácilmente en estudios de Pilates y espacios de entrenamiento en casa."
    ]
  },
  {
    id: "wall-tower",
    name: "Wall Tower",
    fullName: "Wall Tower",
    category: "wall-tower",
    image: "img/wall-tower.jpg",
    portrait: true,
    price: null,
    colors: [],
    description: [
      "La Wall Tower de Maison Reformer combina la versatilidad del entrenamiento con muelles con un diseño vertical que permite aprovechar el espacio. Su panel de madera y sus líneas minimalistas aportan calidez y armonía, tanto en estudios de Pilates como en espacios de entrenamiento en casa.",
      "Incorpora distintos puntos de anclaje, muelles, barras y agarres que amplían las posibilidades de trabajo de fuerza, movilidad y control corporal. Una propuesta funcional para quienes buscan equipamiento de Pilates integrado en un ambiente sereno y acogedor."
    ]
  }
];
