# Cómo poner la web en WordPress con Elementor

## Lo que te llevas

| Archivo | Qué es | Peso |
|---|---|---|
| `calma-elementor.html` | El código para pegar. Las fotos se enlazan desde WordPress. | ~54 KB |
| `calma-elementor-con-fotos.html` | Lo mismo, pero con las fotos metidas dentro. No hay que subir nada. | ~1,5 MB |

Usa el primero salvo que tengas prisa: la web carga mucho más rápido y el
editor de Elementor no se atasca.

## Pasos

**1. Prepara la página**

Crea una página nueva y, antes de nada, en Elementor abre los ajustes de
página (el engranaje de abajo a la izquierda) y pon **Plantilla de página:
Elementor Lienzo**. Eso quita la cabecera y el pie del tema, que si no se
montarían encima del diseño.

**2. Sube las fotos** (solo si usas `calma-elementor.html`)

Medios → Añadir nuevo, y sube estos once archivos de golpe, que así van
todos a la misma carpeta:

    hero.jpg  calma.jpg  barre.jpg  clases.jpg
    est-1.jpg  est-2.jpg  est-3.jpg  est-4.jpg
    retrato.jpg  logo.png  logo-cream.png

Abre cualquiera de ellas en la Biblioteca y copia su dirección. Será algo así:

    https://tudominio.com/wp-content/uploads/2026/08/hero.jpg

**3. Cambia la dirección en el código**

En el archivo, busca y reemplaza todas las apariciones de

    https://TU-DOMINIO.com/wp-content/uploads/calma/

por la parte de tu dirección hasta la última barra, en el ejemplo:

    https://tudominio.com/wp-content/uploads/2026/08/

Con el Bloc de notas o cualquier editor: Buscar y reemplazar, "Reemplazar todo".

**4. Pega el código**

Arrastra un widget **HTML** a la página, borra lo que traiga dentro y pega
el contenido entero del archivo. Publica.

## Si algo sale raro

**Se ve el diseño estrecho, con márgenes a los lados**
El contenedor de Elementor manda. Selecciónalo y ponlo a ancho completo,
con el relleno (padding) a cero.

**Aparece una barra de desplazamiento horizontal**
Lo mismo: contenedor a ancho completo y sin relleno.

**Se ven dos cabeceras**
Falta poner la plantilla en Elementor Lienzo (paso 1).

**Las fotos salen rotas**
La dirección del paso 3 no coincide. Abre una foto en la Biblioteca de
medios, copia su dirección exacta y comprueba que la parte hasta la última
barra es la que has puesto.

## Cuando haya cambios

Los archivos se regeneran con:

    python3 build-elementor.py

Y hay que volver a pegar el código en el widget.
