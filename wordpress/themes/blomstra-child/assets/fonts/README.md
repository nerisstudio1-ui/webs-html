# Tipografías propias

Deja aquí los archivos de fuente y aparecerán solas en el selector de
tipografías de Elementor, dentro de un grupo llamado **Blomstra**. No hay que
tocar código.

## Cómo nombrar los archivos

```
familia-peso-estilo.woff2
```

| Archivo | Se registra como |
|---|---|
| `blomstra-display-400-normal.woff2` | "Blomstra Display", peso 400, redonda |
| `blomstra-display-700-normal.woff2` | "Blomstra Display", peso 700, redonda |
| `blomstra-script-400-italic.woff2` | "Blomstra Script", peso 400, cursiva |

Los guiones del nombre de familia se convierten en espacios y cada palabra se
pone en mayúscula inicial. Valen `.woff2`, `.woff` y `.ttf`; **usa `.woff2`**
siempre que puedas, que pesa la mitad.

## Después de subirlas

1. Elementor → un titular → Estilo → Tipografía → Familia: el grupo **Blomstra**
   aparece arriba del todo.
2. Cámbialas también en los estilos globales, para no ir widget a widget:
   Elementor → hamburguesa → Ajustes del sitio → **Tipografía**.

## Convertir a woff2

Si te dan `.otf` o `.ttf`, conviértelas en [transfonter.org](https://transfonter.org)
marcando solo **WOFF2**. Comprueba antes que la licencia de la fuente permite
uso web (*webfont embedding*): las de escritorio muchas veces no lo incluyen.
