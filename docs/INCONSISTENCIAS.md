# Inconsistencias del diseño que hay que resolver

Cosas que aparecen de forma distinta según el frame. No las he "arreglado" por
mi cuenta: he maquetado lo que se ve y las he listado aquí, porque decidir
cuál es la buena es tuyo. Cada una está ordenada por cuánto bloquea.

---

## 1. Las submarcas no se llaman igual en todas partes — **bloqueante**

| Frame | Submarcas que aparecen |
|---|---|
| Portal escritorio | `01 Blomstra Visual` · `03 Blomstra Experiences` |
| Portal móvil | `Blomstra Weddings` (sin número) · `01 Blomstra Brands` · `02 Blomstra Experiences` |
| Home, sección "Dos formas de habitar Blomstra" | `Blomstra Brands` · `Blomstra Experiences` |
| Página de servicios | `Blomstra Visual` · `Blomstra Experiences` |

Hay tres problemas mezclados:

- **Visual vs Brands**: ¿la primera submarca se llama *Blomstra Visual* o
  *Blomstra Brands*? Aparecen las dos con la misma función.
- **¿Existe Weddings?** Solo sale en el portal móvil. En escritorio hay dos
  paneles, en móvil tres. ¿Weddings es una tercera submarca, o quedó de una
  versión anterior?
- **Numeración**: en escritorio son 01 y 03; en móvil 01 y 02. Falta un 02 en
  escritorio, o sobra el 03.

Esto afecta a la arquitectura del sitio (cuántas secciones, cuántos menús,
cuántas páginas de servicios), así que conviene cerrarlo antes de maquetar más.

## 2. Numeración de la lista de servicios — **bloqueante menor**

En la página de servicios la lista sale con estos números:

```
01  Identidad visual
03  Diseño web
02  Experiencia de marca
02  Dirección d’art
```

Se repite el 02 y falta el 04. Lo he dejado tal cual en el prototipo para que
se vea, pero asumo que la intención es 01, 02, 03, 04. Confírmalo.

## 3. El pie no lleva los mismos enlaces

| Escritorio | Móvil |
|---|---|
| CONTACT US | CONTACT US |
| BEHIND BLOMSTRA | MEET THE FOUNDER |
| NEWSLETTER | BLOG |
| — | NEWSLETTER |

En móvil hay cuatro enlaces y dos no coinciden. ¿"BEHIND BLOMSTRA" y "MEET THE
FOUNDER" son la misma página? ¿Y hay blog?

## 4. El portal invierte el tema en móvil

En escritorio el portal va sobre greige (`NATURAL COTTON`), con el logotipo y
las líneas divisorias **en blanco**. En móvil va sobre crema (`ANTIQUE`), con
logotipo y líneas **oscuros**, la línea bajo el header es gruesa y desaparece
el botón de WhatsApp.

Está reproducido tal cual, pero es un cambio grande para ser solo responsive.
Si es intencionado, perfecto; si no, hay que unificar.

## 5. El botón del header pone "WHATS"

Aparece así en todos los frames, dentro de una cápsula que tiene sitio de
sobra. Parece un texto recortado de "WHATSAPP". Lo he dejado como "WHATS" para
no inventar, pero cámbialo si era eso.

## 6. "Direcció d'art" está en catalán

El resto de la web está en español. En la lista de servicios aparece
*Direcció d'art* en vez de *Dirección de arte*. ¿Errata, o el sitio va a ser
multiidioma y se coló?

## 7. Dos paletas conviviendo

El diseño tiene un swatch de marca (ANTIQUE, NATURAL COTTON, DUSKY GREEN,
TERRACOTTA + dos tonos con la etiqueta cortada) y otro swatch distinto,
etiquetado en francés (VERT MOUSSE, SABLE CHAUD, TERRE CUIVRÉE, VERT D'EAU,
MARRON ANCRÉ, BLEU HORIZON).

Al principio parecía que el segundo era **contenido** —un ejemplo de paleta
mostrado dentro de la web—, pero `BLEU HORIZON` (#C0C5D9) se usa como fondo de
panel en una de las páginas de servicio. Así que o es parte del sistema, o ese
panel está usando un color que no le toca.

He metido las dos paletas en el kit. Dime cuál manda.

## 8. Faltan los hex de dos colores de marca

En la captura del swatch, los dos tonos de abajo (un oliva y un marrón muy
oscuro) tenían la etiqueta cortada. El marrón oscuro es importante: es el
fondo de las secciones de contraste de la home. Los tengo aproximados como
`#8A6B35` y `#33261C`. Mándame esos dos hex.
