# 🎧 Digital Audio Renamer

**Digital Audio Renamer** es una herramienta diseñada para profesionales del sonido, productores de audio y cualquier persona que trabaje con grandes cantidades de archivos de audio. Esta aplicación permite renombrar archivos .wav de forma eficiente, flexible y personalizada, facilitando la organización y el manejo de archivos en proyectos de grabación y edición de sonido.

## 🚀 Características

- **Renombrado personalizable**: Decide si quieres usar un **prefijo**, **sufijo** o ambos, siempre con un número central que se puede ajustar en longitud.
- **Opciones de orden**: Renombra los archivos según el **orden alfabético**, **fecha de creación** o **fecha de última modificación**.
- **Guion bajo opcional**: Incluye o excluye guiones bajos ('_') entre los elementos del nombre de archivo con un simple checkbox.
- **Interfaz gráfica intuitiva**: Usa una interfaz gráfica creada con **Tkinter** que permite seleccionar el directorio y los ajustes de renombrado de manera visual y sencilla.
- **Soporte para múltiples archivos**: Renombra lotes completos de archivos .wav con solo unos pocos clics.

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Tkinter** para la interfaz gráfica.
- **os** y **shutil** para la gestión de archivos.
  
## 🎯 Objetivos

Este proyecto fue desarrollado con el objetivo de hacer más eficiente el flujo de trabajo de renombrado de archivos de audio, especialmente en situaciones donde el orden y la estructura de nombres es crucial para mantener la organización en proyectos de sonido complejos.

## 📋 Requisitos de instalación

1. Asegúrate de tener Python 3 instalado.
2. Instala las dependencias necesarias ejecutando:

   ```bash
   pip install -r requirements.txt
   ```

Nota: No hay muchas dependencias externas, pero asegúrate de tener una versión actualizada de Python.

## 💻 Uso
Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/mario-sound/digitalaudiorenamer
   ```

Navega hasta el directorio del proyecto:

   ```bash
   cd Digital-Audio-Renamer
   ```

Ejecuta la aplicación con:
   
   ```bash
   python main.py
   ```

Usa la interfaz para seleccionar el directorio, el número de dígitos y las opciones de prefijo/sufijo para renombrar los archivos según tus necesidades.

## 📂 Estructura del proyecto

```
Digital-Audio-Renamer/
│
├── img/                   # Logo y otros recursos gráficos
├── code/                  # Código fuente del programa
│   ├── renamer.py         # Lógica de renombrado
│   ├── main.py            # Archivo principal que ejecuta la interfaz gráfica
│   └── rename_by_list.py  # Funciones de utilidad
├── README.md              # Este archivo
```

## ✨ Licencia
Este proyecto está bajo una Licencia para uso docente. Los sonidos y archivos incluidos son solo muestras y no se pueden utilizar sin el permiso expreso de los autores.

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar esta herramienta, no dudes en hacer un fork y abrir un pull request.

## 📧 Contacto
Si tienes alguna pregunta o deseas colaborar, puedes contactarme en:

Correo: info@digitalaudiotips.com
