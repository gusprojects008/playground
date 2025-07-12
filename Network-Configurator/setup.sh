#!bin/bash

echo "Install required resources ..."
pacman -Syu --noconfirm python python-pip iproute2 iw

echo "Creating python enviroment to execute program ***MORE SECURE***"
VENV_DIR="venv_netconfig"
python -m venv $VENV_DIR

echo "Activate python enviroment ..."
source $VENV_DIR/bin/activate

echo "Installing requirements.txt ..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup succefully success!"
echo "To execute the program, RUN:"
echo "==> source $VENV_DIR/bin/activate"
echo "==> python main.py"

