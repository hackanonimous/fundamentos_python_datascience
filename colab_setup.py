import sys
import os

if 'google.colab' in sys.modules:
    # Ejecutando en Google Colab
    os.system("!pip install -U -q ipykernel")
    if not os.path.exists('/root/.local/share/jupyter/kernels/python3'):
        os.system("!python -m ipykernel install --user --name=python3 --display-name=Python 3")