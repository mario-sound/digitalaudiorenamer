import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from renamer import renamer

def select_path():
    """Abrir cuadro de diálogo para seleccionar carpeta"""
    path = filedialog.askdirectory(title="Selecciona el directorio")
    if path:
        path_entry.delete(0, tk.END)  # Limpiar cualquier texto anterior
        path_entry.insert(0, path)  # Insertar el path seleccionado

def start_renaming(event=None):
    """Iniciar el proceso de renombrado"""
    path = path_entry.get()  # Obtener la ruta del cuadro de entrada
    try:
        # Obtener el número de dígitos y validar que sea un entero
        lendigits = int(digit_entry.get())  # Obtener el número de dígitos

        # Obtener el prefijo y sufijo, si están vacíos se dejan como cadenas vacías
        prefix = prefix_entry.get() or ""
        sufix = sufix_entry.get() or ""
        
        if not path:
            raise ValueError("Debe seleccionar un directorio.")
        
        # Verificar el estado de los checkboxes de guion bajo
        use_underscore_before = underscore_before_var.get()
        use_underscore_after = underscore_after_var.get()

        # Obtener la opción de ordenamiento seleccionada
        sort_option = sort_option_var.get()

        # Llamar a la función de renombrado
        renamer(path, lendigits, prefix, sufix, use_underscore_before, use_underscore_after, sort_option)
        messagebox.showinfo("Éxito", "Archivos renombrados correctamente")
    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")

def update_label_prefix():
    """Actualizar el contenido del label dependiendo del estado del checkbox para el prefijo"""
    if underscore_before_var.get():
        prefix_label_underscore_test.config(text="prefix_0001...")
    else:
        prefix_label_underscore_test.config(text="prefix0001...")

def update_label_sufix():
    """Actualizar el contenido del label dependiendo del estado del checkbox para el sufijo"""
    if underscore_after_var.get():
        sufix_label_underscore_test.config(text="...0001_sufix")
    else:
        sufix_label_underscore_test.config(text="...0001sufix")

# Crear la ventana principal
root = tk.Tk()
root.title("Digital Audio Renamer")
root.geometry("550x500")

# Crear un frame para organizar los widgets
main_frame = ttk.Frame(root, padding="10 10 20 20", relief="raised")
main_frame.grid(column=0, row=0, padx=10, pady=10)

# Estilos
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#d9d9d9")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TEntry", padding=5)

# Etiqueta para la ruta
path_label = tk.Label(root, text="Selecciona el directorio:")
path_label.grid(row=0, column=0, padx=10, pady=10)
# Campo de texto para mostrar la ruta seleccionada
path_entry = tk.Entry(root, width=20)
path_entry.grid(row=0, column=1, padx=10, pady=(10,0))
# Botón para seleccionar el directorio
path_button = tk.Button(root, text="Seleccionar", command=select_path)
path_button.grid(row=1, column=1, padx=10, pady=(0, 10))

# Etiqueta para el número de dígitos
digit_label = tk.Label(root, text="Número de dígitos:")
digit_label.grid(row=2, column=0, padx=10, pady=10)
# Campo de texto para introducir el número de dígitos
digit_entry = tk.Entry(root, width=20)
digit_entry.grid(row=2, column=1, padx=10, pady=10)

# Etiqueta para el prefijo
prefix_label = tk.Label(root, text="Prefijo:")
prefix_label.grid(row=3, column=0, padx=10, pady=10)
# Campo de texto para introducir el prefijo
prefix_entry = tk.Entry(root, width=20)
prefix_entry.grid(row=3, column=1, padx=10, pady=10)

# Etiqueta para el sufijo
sufix_label = tk.Label(root, text="Sufijo:")
sufix_label.grid(row=5, column=0, padx=10, pady=10)
# Campo de texto para introducir el sufijo
sufix_entry = tk.Entry(root, width=20)
sufix_entry.grid(row=5, column=1, padx=10, pady=10)

# Checkbox para decidir si usar el guion bajo antes del número (prefijo)
underscore_before_var = tk.IntVar()  # Variable para almacenar el estado del checkbox
underscore_before_check = tk.Checkbutton(root, text="Underscore", fg="gray", font=("Helvetica", 10, "italic"), variable=underscore_before_var, command=update_label_prefix)
underscore_before_check.grid(row=3, column=2, padx=10, pady=5)

# Label que cambiará dependiendo del estado del checkbox para el prefijo
prefix_label_underscore_test = tk.Label(root, text="prefix0001...", fg="gray", font=("Helvetica", 10, "italic"))  # Valor por defecto
prefix_label_underscore_test.grid(row=4, column=1, padx=0, pady=5)

# Checkbox para decidir si usar el guion bajo después del número (sufijo)
underscore_after_var = tk.IntVar()  # Variable para almacenar el estado del checkbox
underscore_after_check = tk.Checkbutton(root, text="Underscore", fg="gray", font=("Helvetica", 10, "italic"), variable=underscore_after_var, command=update_label_sufix)
underscore_after_check.grid(row=5, column=2, padx=0, pady=5)

# Label que cambiará dependiendo del estado del checkbox para el sufijo
sufix_label_underscore_test = tk.Label(root, text="...0001sufix", fg="gray", font=("Helvetica", 10, "italic"))  # Valor por defecto
sufix_label_underscore_test.grid(row=6, column=1, padx=10, pady=5)

# Opciones de ordenamiento
sort_option_var = tk.StringVar(value="alfabetico")  # Opción por defecto
sort_option_label = tk.Label(root, text="Ordenar archivos por:")
sort_option_label.grid(row=7, column=0, padx=10, pady=10)
# Menú desplegable para elegir la opción de ordenamiento
sort_option_menu = tk.OptionMenu(root, sort_option_var, "alfabetico", "creacion", "modificacion")
sort_option_menu.config(fg="black", activebackground="black", highlightbackgroun="grey", font=("Helvetica"), justify='center')
sort_option_menu.grid(row=7, column=1, padx=10, pady=10)

# Botón para iniciar el renombrado
rename_button = tk.Button(root, text="Renombrar", command=start_renaming)
rename_button.grid(row=8, column=1, padx=10, pady=20)

# Vincular la tecla Enter para activar el botón "Renombrar"
root.bind("<Return>", start_renaming)

# Cargar imagen del logo
logo = tk.PhotoImage(file="/Users/mariosanchezmolina/Documents/ConquerBlocks/Python/_Proyectos/Tools/FileRenamer/img/DATlogo.png").subsample(4,4)
# Crear un Label para mostrar la imagen
logo_label = tk.Label(root, image=logo)
# Colocar el Label en la esquina superior izquierda (fila 0, columna 0)
logo_label.grid(row=8, column=2, sticky="se", padx=10, pady=10)

text_sign_label = tk.Label(root, text="Digital Audio Dev. 2024", fg="gray", font=("Helvetica", 10, "italic"))
text_sign_label.grid(row=8, column=0, sticky="sw", padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
