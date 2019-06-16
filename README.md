# Gallery
A web application that users can post photos on various categories. 
## By
* [Rewel Kinyanjui](https://Doktatech.github.io/Gallery/)

## User stories

The user should be able to:

+ [x] View different photos that interest them.
+ [x] Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
+ [x] Search for different categories of photos. (ie. Travel, Food)
+ [x] Copy a link to the photo to share with my friends.
+ [x] View photos based on the location they were taken.

## Prerequisites
+ [x] Python3.6

## Features In Gallery
+ [x] search functionality based on image description.
+ [x] Bootstrap image model and copy link button.
+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Filter images based on category

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/Doktatech/Gallery.git
    $ cd Gallery
    $ python3.6 manage.py --without-pip virtual
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```

## Hot to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```
## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

## License ([MIT License]
This project is licensed under the MIT Open Source license, (c) [Rewel Kinyanjui](https://github.com/Doktatech)