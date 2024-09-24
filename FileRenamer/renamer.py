import os

def get_creation_time(file_path):
    """Obtener el tiempo de creación del archivo"""
    return os.path.getctime(file_path)

def get_modification_time(file_path):
    """Obtener el tiempo de última modificación del archivo"""
    return os.path.getmtime(file_path)

def renamer(path, lendigits, prefix, sufix, use_underscore_before, use_underscore_after, sort_option):
    i = 1
    
    # Obtener la lista de archivos .wav
    files = [f for f in os.listdir(path) if f.endswith(".wav")]

    # Ordenar archivos según la opción seleccionada
    if sort_option == "alfabetico":
        files = sorted(files)
    elif sort_option == "creacion":
        files = sorted(files, key=lambda f: get_creation_time(os.path.join(path, f)))
    elif sort_option == "modificacion":
        files = sorted(files, key=lambda f: get_modification_time(os.path.join(path, f)))

    total_files = len(files)
    num_digits = max(len(str(total_files)), lendigits)
    
    for filename in files:
        # Construir el número con los dígitos especificados
        num_str = str(i).zfill(num_digits)

        # Agregar "_" antes y después del número si están activados
        prefix_part = f"{prefix}_" if prefix and use_underscore_before else prefix
        sufix_part = f"_{sufix}" if sufix and use_underscore_after else sufix

        my_dest = f"{prefix_part}{num_str}{sufix_part}.wav"

        my_source = os.path.join(path, filename)
        my_dest_path = os.path.join(path, my_dest)

        # Evitar sobrescribir archivos
        while os.path.exists(my_dest_path):
            i += 1
            num_str = str(i).zfill(num_digits)
            prefix_part = f"{prefix}_" if prefix and use_underscore_before else prefix
            sufix_part = f"_{sufix}" if sufix and use_underscore_after else sufix
            my_dest = f"{prefix_part}{num_str}{sufix_part}.wav"
            my_dest_path = os.path.join(path, my_dest)

        os.rename(my_source, my_dest_path)
        print(f"Renombrado: {my_source} a {my_dest_path}")

        i += 1
