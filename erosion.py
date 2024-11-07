import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def filtro_erosion_minimo(imagen: Image, matriz_size=3):
    ancho, alto = imagen.size
    nueva_imagen = imagen.copy().convert('L')
    imagen_tonos_gris = imagen.convert('L')
    
    step = matriz_size // 2

    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            bloque = imagen_tonos_gris.crop((x - step, y - step, x + step + 1, y + step + 1))
            minimo = np.min(np.array(bloque))
            nueva_imagen.putpixel((x, y), int(minimo))

    return nueva_imagen

def filtro_erosion_maximo(imagen: Image, matriz_size=3):
    ancho, alto = imagen.size
    nueva_imagen = imagen.copy().convert('L')
    imagen_tonos_gris = imagen.convert('L')
    
    step = matriz_size // 2

    for x in range(step, ancho - step):
        for y in range(step, alto - step):
            bloque = imagen_tonos_gris.crop((x - step, y - step, x + step + 1, y + step + 1))
            maximo = np.max(np.array(bloque))
            nueva_imagen.putpixel((x, y), int(maximo))

    return nueva_imagen

def cargar_imagen():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if filepath:
        global imagen_original
        imagen_original = Image.open(filepath)
        img_tk = ImageTk.PhotoImage(imagen_original)
        lbl_imagen.config(image=img_tk)
        lbl_imagen.image = img_tk

def aplicar_filtro_minimo():
    if imagen_original:
        imagen_filtrada = filtro_erosion_minimo(imagen_original)
        img_tk = ImageTk.PhotoImage(imagen_filtrada)
        lbl_imagen.config(image=img_tk)
        lbl_imagen.image = img_tk

def aplicar_filtro_maximo():
    if imagen_original:
        imagen_filtrada = filtro_erosion_maximo(imagen_original)
        img_tk = ImageTk.PhotoImage(imagen_filtrada)
        lbl_imagen.config(image=img_tk)
        lbl_imagen.image = img_tk

# Interfaz con Tkinter
ventana = tk.Tk()
ventana.title("Filtro de Erosión")

imagen_original = None

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_cargar = tk.Button(frame_botones, text="Cargar Imagen", command=cargar_imagen)
btn_cargar.grid(row=0, column=0, padx=5)

btn_filtro_minimo = tk.Button(frame_botones, text="Filtro Erosión Mínimo", command=aplicar_filtro_minimo)
btn_filtro_minimo.grid(row=0, column=1, padx=5)

btn_filtro_maximo = tk.Button(frame_botones, text="Filtro Erosión Máximo", command=aplicar_filtro_maximo)
btn_filtro_maximo.grid(row=0, column=2, padx=5)

lbl_imagen = tk.Label(ventana)
lbl_imagen.pack(pady=10)

ventana.mainloop()
