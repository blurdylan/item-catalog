# Item Catalog Web App
This web app is a project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Repo
This project has one main Python module `project.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `database_init.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.

## Skills Honed
1. Python
2. HTML
3. CSS
4. OAuth
5. Flask Framework

## Installation
There are some dependancies and a few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal
6. The app imports requests which is not on this vm. Run sudo pip install requests
7. Setup application database `python db_setup.py`
8. *Insert fake data `python db_init.py`
9. Run application using `python main.py`
10. Access the application locally using http://localhost:5000

*Optional step(s)

## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/catalog'
9. Select Create
10. Search for the words 'change this' in login.html and base.html
10. Copy the Client ID and paste it into the `<meta name="google-signin-client_id">`.

## Using the catalog
You can access(edit, delete) the items in the catalog by clicking on the items in a specific category

## JSON Endpoints
The following are open to the public:

Catalog JSON: `/JSON`
    - Displays the whole catalog. Categories and all items.
Category JSON: `/category/<categoryID>/json`
Item JSON: `/category/<categoryID>/<itemID>/json`

## References
- CSS : https://codepen.io/romswellparian/pen/emByWV
