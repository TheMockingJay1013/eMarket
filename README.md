# eMarket

A website for buying and selling used items , made using HTML , CSS and Django

## Features of the website 
This website allows users to : 
- login / logout
- View the different items put up for sale and inspect them in detail
- sell their own products by uploading product details to the website
- contact sellers and have conversations with them reagarding the product
- filter products based on product categeory or search result


## Installation Steps

- Download the files to your device by creating a clone of this project.
  
  On a new terminal , run the command
  ```
  git clone https://github.com/TheMockingJay1013/eMarket.git
  ```
- To install Django run
  ```
  pip install Django
  ```
- Also install pillow by
  ```
  pip install Pillow
  ```
- move to the directory of the project using cd commands

- make the migrations using the commands
  ```
  python manage.py makemigrations
  python manage,py migrate
  ```
- Run the server using the command
  ```
  python manage.py runserver
  ```
- Open this link to view the website [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
