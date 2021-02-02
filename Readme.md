# Project
sudo apt install python3-venv
sudo apt install python3-dev

python3 -m venv venv
source venv/bin/activate

pip3 install wheel
pip3 install python-jose
pip3 install -r requirements.txt

# DataBase
sudo apt install mongodb-server
Set connection_string variable a value equal "localhost:27017"

# Launch
python main.py