# Tipografías con licencia

Aquí van los archivos de **Hatton** y **Agrandir**, de
[Pangram Pangram](https://pangrampangram.com). Las dos son de pago y no
están en el repositorio.

## Qué hay que comprar

Una **licencia de uso web (webfont)** para cada una. La de escritorio no
sirve: son licencias distintas y la web necesita la de web. Suele venderse
por tramos de visitas mensuales, así que para una web de autora basta el
tramo más bajo.

De cada familia hacen falta pocos cortes:

| Familia | Cortes necesarios |
|---|---|
| Hatton | Light y Medium |
| Agrandir | Regular y Medium |

## Cómo instalarlas

Descomprimir lo que envíe la fundición, coger los `.woff2` y dejarlos en
esta carpeta **con estos nombres exactos**:

```
hatton-light.woff2
hatton-medium.woff2
agrandir-regular.woff2
agrandir-medium.woff2
```

Y después, en `assets/css/fonts.css`, quitar el `/*` y el `*/` que envuelven
el bloque 1 (está señalado). Eso es todo: el resto del CSS ya apunta a
ellas. Van comentadas porque, sin los archivos, cada visita se llevaría
cuatro errores 404.

Si la fundición solo entrega `.otf` o `.ttf`, hay que convertirlos a
`.woff2` (cualquier conversor de webfonts lo hace). El `.woff2` pesa
bastante menos y es el formato que entienden todos los navegadores
actuales.

## Sustitutas mientras tanto

| De pago | Sustituta libre |
|---|---|
| Hatton | Instrument Serif |
| Agrandir | Archivo |

Se parecen en proporción y en color de página, pero **no son las mismas**.
La maqueta sirve para juzgar estructura y espaciado, no para dar por buena
la tipografía definitiva.
