import os
from PIL import Image

def convert_tif_to_jpg(tif_path):
    try:
        # Abrir o arquivo .tif
        img = Image.open(tif_path)
        # Salvar como .jpg no mesmo diretório
        new_path = os.path.splitext(tif_path)[0] + ".jpg"
        img.convert('RGB').save(new_path, "JPEG")
        print(f"Convertido: {tif_path} -> {new_path}")
    except Exception as e:
        print(f"Erro ao processar {tif_path}: {e}")

def main():
    root_dir = "feitos"

    # Percorre todo o diretório "feitos"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.tif'):
                tif_path = os.path.join(root, file)
                convert_tif_to_jpg(tif_path)

if __name__ == "__main__":
    main()
