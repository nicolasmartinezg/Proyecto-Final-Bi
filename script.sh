#!/bin/bash
sudo apt-get install git
git config --global user.name "nicolasmartinezg"
git config --global user.email "nicolasmartinezg22@gmail.com"
git clone https://github.com/nicolasmartinezg/Proyecto-Final-Bi.git
sudo apt-get install python3
pip3 install pandas
pip3 install requests
pip3 install boto3
cd Proyecto-Final-Bi
chmod 777 main.py
./main.py

