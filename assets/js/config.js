/* ==========================================================================
   CONFIGURACIÓN — datos que cambian de un vistazo
   --------------------------------------------------------------------------
   Todo lo que hay que confirmar con la clienta está aquí reunido.
   ========================================================================== */

window.CONFIG = {
  /* Teléfono de WhatsApp. Confirmado por la clienta.
     Se guarda en formato internacional y sin signos, que es lo que pide
     wa.me; la versión bonita que se ve en pantalla se compone sola. */
  whatsapp: "34645764616",

  /* Email de contacto. Confirmado por la clienta.
     Es a la vez el que se muestra en pantalla y al que FormSubmit envía
     los mensajes del formulario. */
  email: "cfalconmaldonado@gmail.com",

  /* Servicio del formulario. FormSubmit no necesita servidor: envía a este
     email. Hay que activarlo una vez (ver README). */
  formEndpoint: "https://formsubmit.co/ajax/",

  /* Idioma por defecto */
  idiomaPorDefecto: "es"
};
