import os
from PIL import Image

def optimizar_imagenes(ancho_objetivo=50):
    # Carpeta de entrada y salida
    input_dir = '../'  # <--- Cambia esto por tu ruta
    output_dir = './imagenes_50px'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.webp'):
            path_input = os.path.join(input_dir, filename)
            path_output = os.path.join(output_dir, filename)

            with Image.open(path_input) as img:
                # Calculamos el alto proporcional para no deformar la imagen
                w_percent = (ancho_objetivo / float(img.size[0]))
                h_size = int((float(img.size[1]) * float(w_percent)))

                # Redimensionamos usando LANCZOS para mantener la mejor calidad posible a ese tamaño
                img_resizada = img.resize((ancho_objetivo, h_size), Image.Resampling.LANCZOS)
                
                # Guardamos con optimización activada
                img_resizada.save(path_output, 'WEBP', quality=80, optimize=True)
                print(f"Procesado: {filename} -> {ancho_objetivo}px")

if __name__ == "__main__":
    optimizar_imagenes()