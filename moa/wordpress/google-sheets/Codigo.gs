/**
 * MOA · Guardar las consultas del formulario de la web en esta hoja de cálculo.
 *
 * Instrucciones completas en wordpress/FORMULARIO-GOOGLE-SHEETS.md.
 * Se pega en Extensiones → Apps Script de la hoja y se implementa como
 * aplicación web (acceso: «Cualquier usuario»).
 */

// Correo al que llega un aviso con cada consulta nueva. Vacío ('') para no avisar.
var AVISO_EMAIL = 'patriciadoradotrainer@gmail.com';

var COLUMNAS = ['Fecha', 'Nombre', 'Teléfono', 'Servicio', 'Mensaje', 'Enviado por', 'Idioma', 'Página'];

function doPost(e) {
  var p = (e && e.parameter) || {};
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (hoja.getLastRow() === 0) {
    hoja.appendRow(COLUMNAS);
    hoja.getRange(1, 1, 1, COLUMNAS.length).setFontWeight('bold');
    hoja.setFrozenRows(1);
  }
  // Recorta cada campo para que nadie pueda llenar la hoja con textos enormes
  var corta = function (v, n) { return String(v || '').slice(0, n); };
  var fila = [
    new Date(),
    corta(p.nombre, 120),
    corta(p.telefono, 40),
    corta(p.servicio, 120),
    corta(p.mensaje, 3000),
    p.via === 'mail' ? 'Correo' : 'WhatsApp',
    corta(p.idioma, 5),
    corta(p.pagina, 300)
  ];
  // Evita que un texto que empiece por = + - @ se interprete como fórmula
  fila = fila.map(function (v) { return typeof v === 'string' && /^[=+\-@]/.test(v) ? "'" + v : v; });
  hoja.appendRow(fila);

  if (AVISO_EMAIL && fila[1]) {
    MailApp.sendEmail(AVISO_EMAIL, 'Nueva consulta en la web de MOA: ' + fila[1],
      'Nombre: ' + fila[1] + '\nTeléfono: ' + fila[2] + '\nServicio: ' + fila[3] +
      '\n\n' + fila[4] + '\n\nEnviado por: ' + fila[5] + ' · Idioma: ' + fila[6] +
      '\n\nTodas las consultas: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl());
  }
  return ContentService.createTextOutput('ok');
}
