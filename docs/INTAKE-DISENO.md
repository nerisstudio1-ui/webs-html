# Qué necesito del Figma para poder maquetarlo

Este entorno **no puede acceder a figma.com** (bloqueado por la política de red
del contenedor, error 403 en el proxy). No es cuestión de permisos ni de token:
el dominio entero está fuera de alcance, igual que `api.figma.com`.

Por eso necesito que el diseño llegue por otra vía. Cualquiera de estas tres
sirve; están ordenadas de mejor a peor.

---

## Opción A — Exportar los frames como imagen (la más rápida)

En Figma, por cada pantalla del diseño:

1. Selecciona el frame en el panel de capas.
2. Panel derecho → **Export** → formato **PNG**, escala **2x**.
3. **Export <nombre>**.

Necesito, como mínimo:

- La **home completa** (el frame entero, de arriba abajo, no recortado).
- Cada **página interior** que tenga el diseño (nosotros, servicios, contacto…).
- Las versiones **móvil** si existen en el archivo.

Adjunta los PNG en el chat. Con eso puedo reconstruir estructura, jerarquía y
espaciados con bastante fidelidad.

## Opción B — Exportar los tokens exactos (recomendado combinar con A)

Las imágenes me dan la composición, pero los valores exactos se leen mejor así.
En Figma, con **Dev Mode** activado, selecciona un elemento y copia el CSS del
panel derecho. Me interesa sobre todo:

- **Colores**: los HEX de la paleta (Local styles / Variables).
- **Tipografías**: nombre de familia, pesos y tamaños de H1–H6, cuerpo y botón.
- **Anchos**: ancho del frame de escritorio (1440? 1920?) y ancho del contenido.
- **Espaciados**: padding vertical de las secciones.

Pégalos en el chat tal cual, o déjalos en `design-input/tokens.md`.

## Opción C — Exportar el archivo

**File → Export frames to PDF**, o descargar el `.fig`. Súbelo al repo en
`design-input/` y lo leo desde ahí.

---

## Además, cosas que la imagen no me dice

Para no inventármelas, cuéntame:

| Punto | Por qué importa |
|---|---|
| ¿Tienes **Elementor Pro**? | Sin Pro no hay Theme Builder: header y footer no se pueden montar con Elementor y hay que resolverlos por otra vía. |
| ¿WordPress ya está montado y dónde? | Cambia si te entrego un kit para importar o si además hay que configurar el hosting. |
| **Textos reales** o lorem ipsum | Si el Figma lleva texto de relleno, dime el copy definitivo. |
| **Imágenes y logo** | Necesito los originales exportados, no recortes de pantalla. |
| ¿Hay **formulario**, **tienda**, **reservas**, **idiomas**? | Determina qué plugins hacen falta además de Elementor. |
| Fuentes de pago (Adobe Fonts, etc.) | Si no son de Google Fonts hay que subirlas con el uploader de Elementor Pro. |
