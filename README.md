
![flight-typo](https://github.com/Febiecode/Flight-Ticket-Booking/assets/93641901/9fba2638-df8b-46ed-8c88-1cc090ac29cb)
# Website link http://febiecode.pythonanywhere.com/
# FlightHub: A Powerful Flight Booking Application in Django
A flight booking Django application written in Python, HTML, CSS & Javascript.

![home](https://github.com/Febiecode/Flight-Ticket-Booking/assets/93641901/1567cdff-f13c-425a-9c62-052e21b99bbc)

### Admin credential
- username: sathyakumar
- pwd: admin

### Admin Management
  - `Flight` - Models directory. Admin can easily modify and add new records for below models.
    - `Flight` 
    - `Passengers`
    - `Places` 
    - `Tickets`
    - `Users`

### Features
1. Users can create their user account.
2. Users can book both one-way as well as round-trip tickets.
3. Webpages are mobile responsive.
4. Users can cancel their booked tickets.
5. Users can view their previously booked tickets (Both confirmed and cancelled tickets).
6. Tickets are downloadable as pdf document.
7. As-you-type Search

### Files & Directories
  - `capstone` - project directory.
    - `utils.py` - Contains all Django helper functions used in views.py.
    - `urls.py` - This file handles all the URLs of the project.
  - `flight` - main application directory.
    - `static` - contains all static content.
        - `css` - Contains all css files for styling the webpages.
        - `js` - Contains all javascript files used in the application.
        - `img` - Contains all image files used in the application.
    - `templates/flight` Contains all application templates.
        - `book.html` - Template for showing selected flight and reading Travellers data.
        - `bookings.html` - Template for showing bookings done by a user.
        - `index.html` - Home page template.
        - `layout.html` - Base template for all pages except login & register page.
        - `layout2.html` - Base template for login & register page.
        - `login.html` - Login user page.
        - `payment_process.html` - Page after completion of payment.
        - `payment.html` - Payment page.
        - `register.html` - Register user page.
        - `search.html` - Flight search result page.
        - `ticket.html` - Template for printing ticket(pdf).
    - `admin.py` - Contains some models for access to the Django administrator.
    - `models.py` - All models used in the application are created here.
    - `urls.py` - This file handles all the URLs of the web application.
    - `views.py` - This file contains all the application views.
    - `constant.py` - This file contains the fee amount which is charged to the user for booking flight tickets.
  - `requirements.txt` - This file contains all contains all the python packages that needs to be installed to run this web application.
  - `manage.py` - This file is used basically as a command-line utility and for deploying, debugging, or running our web application.

### Justification

1. Mobile responsive webpages.
2. More complex models.
3. More interatactive because webpages use ajax functionality (eg., fetch) written in javascript.
4. Converts html template to downloadable pdf.

### Installation

- Install Python3.9 from [here](https://www.python.org/downloads/) manually.
- Install project dependencies by running `py -m pip install -r requirements.txt`.
- Run the commands `py manage.py makemigrations` and `py manage.py migrate` in the project directory to make and apply migrations.
- Create superuser with `py manage.py createsuperuser`. This step is optional.
- Run the command `py manage.py runserver` to run the web server.
- Open web browser and goto `127.0.0.1:8000` url to start using the web application.


