#! /bin/bash

#Necessary installs
pip3 install Flask
pip3 install requests
from Flask import flask
import flask
echo "Demo for question 1:"
echo "Running python script q1.py...."
python3 q1.py


echo "========================"
echo "========================"



echo "Demo for question 2:"
echo "...."
echo "You should access http://127.0.0.1:5000/ from your URL and pass paramaters like so:"
echo " ..../integer_quantity/label_stock"
echo "========================"

#mkdir sandbox
cd sandbox
python3 -m venv venv
chmod 777 ./venv/bin/activate
./venv/bin/activate

export FLASK_ENV=development
export FLASK_APP=app.py
python3 -m flask run

 
