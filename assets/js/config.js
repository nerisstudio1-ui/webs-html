/* ==========================================================================
   CONFIGURACIÓN — datos que cambian de un vistazo
   --------------------------------------------------------------------------
   Todo lo que hay que confirmar con la clienta está aquí reunido.
   ========================================================================== */

window.CONFIG = {
  /* Teléfono de WhatsApp en formato internacional, sin "+" ni espacios.
     PENDIENTE DE CONFIRMAR: el 645764616 es el teléfono del formulario de
     contacto de Neris Studio. Confirmar con Cristina si es el que quiere
     publicar en la web. */
  whatsapp: "34645764616",

  /* Email al que llegan los mensajes del formulario.
     PENDIENTE: confirmar si usa su email personal o uno nuevo tipo
     contacto@sudominio.com (recomendado). */
  email: "EMAIL@PENDIENTE.com",

  /* Servicio del formulario. FormSubmit no necesita servidor: envía a este
     email. Hay que activarlo una vez (ver README). */
  formEndpoint: "https://formsubmit.co/ajax/",

  /* Idioma por defecto */
  idiomaPorDefecto: "es"
};
