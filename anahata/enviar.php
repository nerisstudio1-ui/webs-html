<?php
/**
 * ANAHATA · Recogida de los formularios de la web
 * ------------------------------------------------
 * Sube este archivo a la raíz del sitio, junto al index.
 * No necesita ningún servicio externo: usa el correo del propio hosting.
 *
 * Si los mensajes no llegan o caen en spam, revisa DESTINO y lee la nota
 * del final sobre el remitente.
 */

// ---- Configuración ----------------------------------------------------
$DESTINO = 'saravgyoga@gmail.com';        // a dónde llegan los mensajes
$VOLVER  = '/';                            // a dónde se devuelve al visitante
// -----------------------------------------------------------------------

// Solo aceptamos envíos del formulario
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . $VOLVER);
    exit;
}

/** Limpia un valor recibido y lo recorta. */
function campo(string $nombre, int $max = 2000): string {
    $v = $_POST[$nombre] ?? '';
    $v = is_string($v) ? trim($v) : '';
    $v = str_replace(["\r", "\n", "%0a", "%0d"], ' ', $v);  // evita cabeceras inyectadas
    return mb_substr($v, 0, $max);
}

/** Vuelve a la web con el resultado. */
function volver(string $estado, string $ancla = 'contacto'): void {
    global $VOLVER;
    header('Location: ' . $VOLVER . '?envio=' . $estado . '#' . $ancla);
    exit;
}

// Trampa para robots: un campo oculto que una persona nunca rellena
if (campo('web') !== '') {
    volver('ok');   // al robot le decimos que todo fue bien
}

$tipo = campo('tipo', 40) === 'newsletter' ? 'newsletter' : 'contacto';

if ($tipo === 'newsletter') {
    $email = filter_var(campo('email', 200), FILTER_VALIDATE_EMAIL);
    if (!$email) {
        volver('error', 'contacto');
    }
    $asunto  = 'ANAHATA · Nueva suscripcion a la newsletter';
    $cuerpo  = "Alguien se ha suscrito a la newsletter desde la web.\n\n";
    $cuerpo .= "Correo: $email\n";
    $responder = $email;
} else {
    $nombre  = campo('nombre', 120);
    $email   = filter_var(campo('email', 200), FILTER_VALIDATE_EMAIL);
    $mensaje = campo('mensaje', 5000);
    if ($nombre === '' || !$email || $mensaje === '') {
        volver('error');
    }
    $asunto  = 'ANAHATA · Consulta de ' . $nombre;
    $cuerpo  = "Nueva consulta desde la web de ANAHATA.\n\n";
    $cuerpo .= "Nombre:   $nombre\n";
    $cuerpo .= "Correo:   $email\n";
    $cuerpo .= "Teléfono: " . (campo('telefono', 40) ?: '(no indicado)') . "\n";
    $cuerpo .= "Interés:  " . (campo('interes', 120) ?: '(no indicado)') . "\n\n";
    $cuerpo .= "Mensaje:\n$mensaje\n";
    $responder = $email;
}

$cuerpo .= "\n---\nEnviado el " . date('d/m/Y \a \l\a\s H:i') . "\n";

// El remitente debe ser del propio dominio: si no, Gmail lo rechaza o lo
// manda a spam. El correo del visitante va en Responder-a.
$dominio = preg_replace('/^www\./', '', $_SERVER['HTTP_HOST'] ?? 'localhost');
$cabeceras = implode("\r\n", [
    'From: ANAHATA <no-reply@' . $dominio . '>',
    'Reply-To: ' . $responder,
    'Content-Type: text/plain; charset=UTF-8',
    'X-Mailer: PHP/' . phpversion(),
]);

$enviado = @mail($DESTINO, '=?UTF-8?B?' . base64_encode($asunto) . '?=', $cuerpo, $cabeceras);

volver($enviado ? 'ok' : 'error', $tipo === 'newsletter' ? 'contacto' : 'contacto');
