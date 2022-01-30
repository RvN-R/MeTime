# [Me Time Minds](https://metimeminds.herokuapp.com/)

## App preview

## Wireframes

![Homepage](/wireframes/homepage.png)

![Homepage after user has logged in](/wireframes/afterlogin.png)

![Journalling page](/wireframes/Journalling.png)

![Journalling page](/wireframes/Pledges.png)

![User profile page](/wireframes/userprofile.png)

This is an app to help people improve their mental health by pledging and journalling changes to help them live a better life.

The app was designed during the Code Instiute January 2022 hackathon.  The 4 Minds team - Richard,  Sandra,  Debbie and Ashley worked together to produce this app over 5 days from January 26th to January 30th 2022.

The app was deployed to heroku and can be accessed by clicking on the title above.   Alternatively here is a link to the [heroku app.](https://metimeminds.herokuapp.com/)

## UX

### User persona

The app is aimed at adults aged over 18 who are working and/or retired and who recognise that managing their stress levels through journaling and pledging could lead to a better life balance and more productivity and enjoyment of life.

## User stories

1. Each user has a unique username chosen by them and password and a user profile showing resources accessed through the app.

2. A user can see a range of resources which could help them with their journaling and pledging on the resources page.

3.  After logging in a user will be able to write a journal entry and make a pledge.

4. If a user is logged out then they will only be able to see the resources page and the about page and a log in button.

5.  Each logged in user  will see a message on the screen stating that they are logged in.

6. A logged in user will be able to view all resources they have accessed over a period of time.


## Design features

* The navbar must appear on every page so that the user can easily navigate between pages.

* The navbar has the title of of the website, "Me Time Minds" on the left hand side.  If a user clicks on this they are taken to the home page.

* The home page shows the following items in the navbar:  "Me Time minds logo", "About Us", "Register/log in", "Resources", "Pledges", "Journaling" and "log out" if the user is logged in.

* The colour pallet chosen was a white background with pastel colours in the foreground,  aimed at being constrasting and calming colours.


## Technologies Used

* [HTML](https://www.w3schools.com/html/) or Hypertext markup language. HTML is used to create the structure of web pages. It consists of tags which tell the browser how to set out text and images on the page. Hypertext is the method by which you move around on the web, markups are the tags which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax. The data in the tags is read by the web browser enabling you to create any web page you like. In this project my templates are all written in HTML. There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about each island. The base template sets out the way in which the website should look and information from this is used in each of the other templates.

* [CSS](https://www.w3schools.com/Css/) stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled. It allows the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

* [Django](https://www.djangoproject.com/) is a web development framework that assists in building and maintaining quality web applications. Django helps eliminate repetitive tasks making the development process an easy and time saving experience.

* [jquery](https://jquery.com/) is used to simplify DOM manipulation. Jquery is a javascript library that is used to provide interactivity on websites. The $ sign signals to the browser that jquery is being used.

* [Python](https://www.python.org/psf-landing/) is a high level programming language used for apps in many frameworks such as flask, pyramid and django. Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries. Python is managed by a non profit organsation the Python software foundation.  The version of Python I used in my app is 3.7.

* We used [Postgres](https://www.postgresql.org/) for the models in our databases, although sqlite3 was available in django. This was because  the app is deployed to heroku and heroku is an ephemeral file system so my data would disappear each time a user logged into heroku! Postgres is an open source object-relational database system that provides the user with the facility to create, read, update and delete documents data.

* [Heroku](https://www.heroku.com/) is a cloud platform that allows a developer to build, deliver, scale and monitor apps. Heroku makes the experience of deploying an app relatively straightforward.

* We used [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/) to work on our code. Chrome dev tools are a set of tools designed to give the developer tools to amend code in a testing environment in order to enhance the UX and functionality experience. We were also able to test the responsiveness of my app using these tools.

* Some of us used [vscode](https://code.visualstudio.com/) as one coding editor and others used [gitpod](https://www.gitpod.io/blog/gitpodify/).  

## Databases used

[SQLite3](https://www.sqlite.org/index.html) is a database provided by django and is the default database for django projects.
[Postgres](https://www.postgresql.org/) is an open source relational database.

Django does not determine a type of database to be used.  We decided to use postgres as heroku is an ephemeral system meaning that data stored in SQLite would disappear each time I accessed the app!

## Data Models used

In Django, data models are the databases which store data about the objects in the database.  The MathsRevisionPlus app used 2 models in addition to the django provided user model which stored details of users.  The models were:

### Pledges model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Name| name |maxlength=254|Charfield
Date|dateofpledge|nomaxlength|Charfield
pledge|pledgemade|nomaxlength|Charfield


### Journal model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Name| name |maxlength=254|Charfield
Date|dateofpledge|nomaxlength|Charfield
pledge|pledgemade|nomaxlength|Charfield


## Testing

Testing was carried out by human beings.

* Manual Testing

We tested each part of my user story to check it worked as expected.


## Interesting bugs or problems  discovered during testing

The most annoying bug we came across was when we were trying to push our code to heroku. We followed the instructions above but got an error 500 after each attempt. Despite looking at our code in detail we couldnt find anything wrong with it. 

We thought about using [travis integrated testing](https://travis-ci.com/) to run automated tests but unfortunately we didnt have time to do this.



## Development process of our project

One member of the team set up a repo which we all cloned locally, created a local repo and a branch on the main repo for each task.  The main repo owner added collaborators to the main repo so that they could approve pull requests when needed.  Git branch protection was also set up.

Each collaborator then created a new django project, called mathsplusrevision in vscode by typing ```django-admin startproject projectname .```  in the terminal as well as a .gitignore folder ready to hold files that we didnt want to push to github.  This .gitignore file held my environmental variables and the vscode settings that didnt need to be pushed to github.

The settings.py file contained the list of apps that were created as part of this project and each app handled a specific piece of functionality. The apps created were accounts, pledges, journal, and products.  We created the  apps using ```python manage.py startapp appname```.  We ran the project throughout the development process by typing ```python manage.py runserver```  each time we added some fucntionality to the project to check whether or not it was working as expected.

We created a requirements file to hold details of all the packages needed to run the app, eg. pillow for images.  As each package was added using ```pip install package```  it was important to remember to update the requirements file.

* media

This folder held pictures of images for the products that would appear on the website.

* pledges

This app  managed the input, storage and output of  pledges made by a user.

* journal

This app  managed the input, storage and output of  pledges made by a user.

* procfile

This file held details of resources users had accessed whilst using the app.

* static folder

We created a static folder for images and styles.css files and a templates folder for  templates.  Next thing was to set up the base template folder with four files inside:  base.html,  and registration.html.

Effects for the nav bar were put into the styles.css file which was in the static folder.

In our virtual environments, we imported all the modules we would need and also put sensitive information like environmental variables in git ignore.   We ensured that the keys could only be accessed from this and not on public display on github. 
 
We created a procifle and requirements file in order for the app to run on heroku.

Lastly we checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly input into the heroku dashboard for the app and that debug was set to false so that the app was secure.

We created a favicon for the app, using a freefavicom creator.

We created wireframes  using [figma](https://www.figma.com/file/NDRePJhgypAgZZvLRq8ThE/Microblog-Design-Page-(Community)?node-id=4%3A2).  

## Deployment

The following section describes the process we undertook to deploy this project to Heroku.

1. We ensured that all required technologies were installed locally, as per the requirements.txtfile.  

2. We ensured that we had created a procfile indicating that my app was based on python.

3. We logged in to Heroku, using 'heroku login' command the we input Heroku login details.

4. We then created a new Heroku app, using heroku ```apps:create appname command```.

5. We pushed our project to github and enabled automatic link to heroku.  This took some time to set up as we had to make sure that our environmental variables were correct.

6.  We then logged into Heroku and selected newly created app.

7. We entered all the environment variables into the heroku panel including: secret key, public key, the host name and the port.

8. The final push to heroku was harder than we thought!  We first had to set  debug to False in the settings.py file in the Me Time Minds app. Then we had to do  ```python manage.py collectstatic```   to successfully transfer all the files heroku needed to run the app across to heroku.

9. We then had to put all our environmental settings in my heroku config vars for my project as shown below.

* DATABASE_URL       xxxxxxxxxx
* IP                 xxxxx
* PORT               xxxxx
* SECRET_KEY         xxxxxxxxx

We checked that the app was now deployed via Heroku

## Breakdown of steps involved in creating the Me Time Minds django app by each collaborator.

 1.  First thing was to clone the project!

 2. First we created a virtual environment and made a .gitignore file.  We then installed django.

 3. We put all the virtual environment files and database access keys into .gitignore so that they would not be pushed to github.

 4.  We then created a new github repo and initialised a local repo for the project and set up a branch for each person to use on the main repo.
 
 
 6. We then created an env file to hold all  passwords for the databases and the secret  key.  This file was put in .gitignore.

 7. We had to remember to create a requirements.txt file as we downloaded different packages for the app as we went along. Pillow was used to handle images and whitenoise for the media files.

 8. We worked on our code and created pull requests when we wanted to add to the main repo. 

 9. It was important to remember to make migrations and then migrate for all the models in each app ```python manage.py makemigrations``` and ```python manage.py migrate```.  

 10. Finally in order to get into the admin panel it was important to create a superuser ```python manage.py createsuperuser```

## Future improvements

 1. App suggests pledges to be made by user based on resources accessed by each user.

 2. Allow user to search resources using tags or words of interest.

 3. Add in a well being blog on developments in managing stress, mental health issues, etc for users.

 4. Include a feature where users can upload images to their journal entry.

 5. Add a password reset feature.

## Credits

* Media

Images on the home and about page were from [freepics](https://www.freepik.com/)

* The idea of creating [a user persona](https://www.romanpichler.com/tools/the-persona-template/) came from a blog read by Roman Pichler, a project management expert who specialises in digital products using Agile and Scrum methodologies.



## Acknowledgements

We received inspiration for this project from  [](/) 

We  used the [django documentation](https://docs.djangoproject.com/en/3.0/) to help us sort things out on a regular basis. 