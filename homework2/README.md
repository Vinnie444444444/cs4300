**Movie Theater Booking Web App for CS4300 HW#2**

This is a Django-based Movie Theater Booking Application that allows users to view movies, book seats, and check their booking history. 
It can be hosted locally or through render. 

- View movie listings via the API
- Book seats via the API
- Check booking history via the API


**Project Structure**

homework2/

├── bookings/ # Django models, views, templates

├── homework2_env/ 

├── movie_theater_booking/ # app folder

├── manage.py 

├── requirements.txt # Python dependencies remove gdp from it

├── render.yaml # render deployment file

├── db.sqlite3 

└── staticfiles/ # Collected static files. Needed to make it format correctly on render

**Setup Instructions**
1. Clone repository
  - git clone https://github.com/Vinnie444444444/cs4300.git
2. Set up Virtual Envioroment
  - python3 -m venv homework2_env
  - source homework2_env/bin/activate
3. Install Requirements
  - pip install -r requirements.txt
4. Run server (locally)
  - python manage.py runserver 0.0.0.0:3000
4.5 Run server through Render
  - Add Blue print through dashboard and connect cloned git repo
  - Change render root to homework2
5. Access
  - Locally: http://localhost:3000/
  - Render: https://movie-theater-booking-3cl2.onrender.com/

**Endpoints** 
There is no functionality to swap between them, so they must be put into the url
1. /api/movies/
2. /api/seats/
3. /api/bookings/

