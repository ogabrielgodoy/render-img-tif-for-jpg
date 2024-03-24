## Conversor TIF para JPG

Este script em Python percorre recursivamente um diretório especificado, localiza todos os arquivos .tif dentro dele e converte cada um para o formato .jpg. A conversão é realizada utilizando a biblioteca Pillow (PIL).

### Como Usar
1. Certifique-se de ter o Python instalado em seu ambiente.
2. Instale a biblioteca Pillow utilizando `pip install pillow`.
3. Edite o diretório raiz no script `app.py` para o diretório que contém os arquivos .tif que deseja converter.
4. Execute o script `app.py`. Os arquivos .tif serão convertidos para .jpg no mesmo diretório.

### Notas
- Os arquivos .tif serão substituídos pelos .jpg convertidos no mesmo diretório. Recomenda-se fazer uma cópia dos arquivos .tif originais antes de executar o script, em caso de falhas.
- Certifique-se de ajustar o diretório raiz 'feitos' para o seu caso específico.

### Requisitos
- Python
- Biblioteca Pillow (PIL) (Execute para instalar: pip install pillow)

### Use no console para executar
```bash
python app.py
