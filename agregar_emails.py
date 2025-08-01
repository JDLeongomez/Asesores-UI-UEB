import os
import re

# Ruta a tu carpeta de autores
carpeta_autores = "content/authors"

for root, dirs, files in os.walk(carpeta_autores):
    for file in files:
        if file == "_index.md":
            ruta = os.path.join(root, file)
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()

            # Salta si ya hay un bloque de email HTML insertado
            if '<b>Email:</b>' in contenido:
                print(f"🔹 Ya existe email en {ruta}")
                continue

            # Busca el email en la línea con mailto:
            match = re.search(r'link:\s*mailto:([^\s]+@unbosque\.edu\.co)', contenido)
            if match:
                email = match.group(1)
                bloque_html = f'\n<p><i class="fas fa-envelope" style="color: #f68212;"></i> <b>Email:</b> {email}</p>\n'
                nuevo_contenido = contenido.strip() + bloque_html  # Strip para evitar líneas vacías excesivas

                with open(ruta, 'w', encoding='utf-8') as f:
                    f.write(nuevo_contenido)

                print(f"✅ Email agregado a {ruta}")
            else:
                print(f"⚠️ No se encontró email en {ruta}")
