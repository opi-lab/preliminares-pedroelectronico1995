# Basic Image Handling and Processing

# Pedro Nel Mendoza Vanegas
Este repositorio es acerca del capítulo 1 del libro guía del curso de Visión Artificial.Los ejemplos y ejercicios que serán desarrollados, están basados en el libro de Erik Solem titulado ``Programming Computer Vision with Python_ Tools and algorithms for analyzing images``.
The contents about repository are the following: 

# Contenido

1. ``ch01-ex1.py``: En este programa para solucionar el ejercicio 1 del capítulo 1 del libro guía, lo que se hace es tomar una imagen cualquiera y aplicarle a ésta un blur gaussiano (desenfoque gaussiano), para ello es necesario que la imagen esté convertida a escala de
grises. Luego de esto, se trazan los contornos de la imagen emborronada aumentando los valores de la desviación estándar (sigma) y se 
grafican dichos contornos.

2. ``ch01-ex2.py``: Se implementa una operación llamada unsharp masking mediante un blurring (emborronado) de una imagen y luego restar la versión de la imagen con blur, de la original. Esto permite dar un efecto de sharpening a la imagen. En este programa, se intenta hacer esta operación tanto para imágenes a color como para escala de grises.

3. ``ch01-example1.py``: En este programa se lee una imagen a color y se realizan varias conversiones y/o procedimientos sobre ella: Conversión a escala de grises, creación de miniaturas, rotación de imagen, recortar una región de una imagen y luego pegarla sobre ella. Esto se hace para 2 de las imágenes de la carpeta data.

4. ``ch01-example2.py``: En este programa se lee una imagen (a color) a un arreglo, se dibujan algunos puntos en coordenadas (x,y) sobre 
una figura donde está graficada la imagen y se dibuja una línea (verde) donde se conectan algunos de estos puntos. Adicionalmente,
se muestra un histograma de la imagen con un número de bins de 10 y otro histograma con 200 bins.

5. ``ch01-example3.py``: En este programa lo que se hace es leer una imagen (a color) a un arreglo, en primera instancia. Después de esto, se imprime una tupla que contiene lo siguiente: filas, columnas, canales de color y el tipo de datos de los elementos del arreglo que contiene la imagen. Este procedimiento también se hace para la imagen convertida a escala de grises, con la diferencia de que el canal de color desaparece. Posterior a esto se imprime el objeto de arreglo y se hacen operaciones sobre él para luego imprimirlas como: Suma de los valores de unas filas y columnas, promedio de una familia, asignación de un valor único a los elementos de una columna, entre otras.






