# Erosión

Implementación de filtro qde erosión una imagen que el usuario escoja para la materia de proceso digital de imágenes.

La erosión es operación en la cual se toma un pixel y sus vecindades, dependiendo de cual se use se asignará ese valor al pixel central.

### Aplicar Filtro Oleo
El filtro erosión se aplica a la imagen de dos maneras:
1. **aplicar filtro minimo**: Aplica el filtro de erosión mínimo en la imagen cargada y muestra el resultado en la interfaz.
2. **aplicar filtro máximo**: Aplica el filtro de erosión máximo en la imagen cargada y muestra el resultado en la interfaz.

## Requisitos

- Python 3.x
- Tkinter
- Pillow

## Uso

1. Ejecuta el script utilizando el comando "erosion.py".
2. Cargar la imagen con el boton "Cargar Imagen"
3. Escoger el filtro a utilizar de la lista de selección