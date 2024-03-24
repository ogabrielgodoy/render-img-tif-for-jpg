import os
from PIL import Image

# Variável para configurar o nome da pasta de exportação
pasta_exportacao = "export"
# Diretório raiz onde o código deve começar a busca
root_dir = "feitos"

def convert_tif_to_jpg(tif_path):
    try:
        # Abrir o arquivo .tif
        img = Image.open(tif_path)
        
        # Criar pasta 'export' se ainda não existir
        export_dir = os.path.join(os.path.dirname(tif_path), pasta_exportacao)
        os.makedirs(export_dir, exist_ok=True)
        
        # Salvar como .jpg na pasta 'export'
        new_path = os.path.join(export_dir, os.path.splitext(os.path.basename(tif_path))[0] + ".jpg")
        img.convert('RGB').save(new_path, "JPEG")
        print(f"Convertido: {tif_path} -> {new_path}")
    except Exception as e:
        print(f"Erro ao processar {tif_path}: {e}")

def main():
    # Percorre todo o diretório "feitos"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.tif'):
                tif_path = os.path.join(root, file)
                convert_tif_to_jpg(tif_path)

if __name__ == "__main__":
    main()
