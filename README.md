# My Memoirs


## Description
A personal gallery application that displays my photos for others to see. You can visit the live site on `https://my-memoirs.herokuapp.com/`


## Author


* [**Brian Major**](https://github.com/bryomajor)

## Features


As a user of the web application you will be able to:

1. See all posted photos
2. View photos by location
3. See each photo's description and location on hover.
4. Be able to copy a photo's url to the clipboard
5. Click on `view image` to expand a photo
6. Search for a photo by category e.g. _outdoor_, _photoshoot_

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View all posted photos  | Hover over a photo | Shown details about the photo | 
Details about the photo | Click on `Copy Link` | Pop up that shows that the image link has been copied appears |
|  Details about the photo | Click on `View Image`  | Photo expands |
|  Search in the search field | Input keywords to be searched then press ENTER | Search page is loaded and displays with the searched results |


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/bryomajor/memoirs.git
        $ cd memoirs

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations photos
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py test photos
        
## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Django](https://www.djangoproject.com/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)


## Support and Team
Brian Major


[Slack Me!](https://slack.com/intl/en-ke/)  @bryomajor


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
