# The Lady Goldsmith
## **Code Institute - Portfolio Project 5: _E-commerce Application_** 
The Lady Goldsmith! is an online e-commerce fine jewellery store.

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes.
## Demo

[View the Live Website Here](###############)

<img src="###############">


## Table of contents
+ [User Experience](#User-Experience)
     + [Project Goals](#Project-Goals)
     + [User Stories](#User-Stories)
     + [Strategy](#Strategy)
     + [Scope](#Scope)
     + [Structure](#Structure)
          + [Front end Pages](Front-end-Pages)
     + [Skeleton](#Skeleton)
          + [Wireframes](#Wireframes)
     + [Surface](#Surface)
+ [Features](#Features) 
     + [Existing Features](#Existing-Features)
     + [Features to Implement in the future](#Features-to-Implement-in-the-future)
+ [Database](#Database)
+ [Technologies Used](#Technologies-Used)
     + [General Resources](#General-Resources)
     + [Tools](#Tools)
+ [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
+ [Deployment](#Deployment)
     + [Heroku Deployment](#Heroku-Deployment)
     + [Forking the Repository](#Forking-the-Repository)
     + [Making a Local Clone](#Making-a-Local-Clone)
+ [Credits](#Credits)

***
# User Experience
## Project Goals
The primary goal of The lady Goldsmith is to enable users to purchase jewellery through an fully functional ecommerce website. The goal for the design was to make it as easy as possible to access information, while striving for a minimalist and user-friendly layout.

## User Stories
**As a Casual User, I want to:**

1. 

**As a Registered User, I want to:**

1. 

**As an Administrative Account holder, I want to:**

1. 

<br>

[^ back to top ^](#Table-of-contents)
<br>

## Strategy
### — Project Planning —

 Agile development was implemented from the onset of this project and simply explained Agile is an iterative approach to project management and software development that helps teams deliver value to their customers, faster and with fewer headaches. Instead of betting everything on a "big bang" launch, an agile team delivers work in small, but consumable, increments. As the development team for this project was a single developer I attempted to use this approach for building this project.  
 <br>
 The methodology requires a detailed and thorough project planning process, to design and create a web-based interactive application.I distinguished the required functionality of the site and how it would answer the user stories, as described above, these user stories were then developed through the use of the Five Development Planes framework. To keep track of my development I created a user stories kanban board in github projects. I created an issue for each user story which was set to automatically display in my user story project. As I worked each user story, it was moved to the in progress column and finally into the completed column once it was complete.  
<br>
 The design of the website is meaningful and simple so that the purpose of the website is very clear for first-time users, and they can easily adapt to the website. This also applies to all the functions to create, post, edit and delete porducts for the Admin/site owners. The owner’s main goal is to provide a ecommerce platform that is easy to use whether they are first-time or returning users, and this is the key to grow the community for further business opportunities. To achieve this, the website is designed and created by users first concept.

The functions on the tables below are minimum requirements for the website to achieve the current user's and owner's goals. On a scale of 1  - 5 

| Opportunity                                 | Importance | Viability / Feasibility |
| :------------------------------------------ | :--------: | :---------------------: |
| Register                                    |           |                        |
| Login / Log out                             |           |                        |
| Categories page                             |           |                        |
| Search by Category                          |           |                        |
| Create / Edit / Delete                      |           |                        |
| Search Products By Keywords                 |           |                        |
| Review By Other Users                       |           |                        |
| Wishlist                                    |           |                        |
| Responsiveness                              |           |                        |
| Page 404                                    |           |                        |

Below are the additional functions that can improve the website, however, these are not mandatory to achieve the current user's and owner's goals. Some are not implemented due to a lack of my current skills & knowledge and also due to a lack of time allocated for this project.

| Opportunity                             | Importance | Viability / Feasibility |
| :-------------------------------------- | :--------: | :---------------------: |
| Resetting Password When Users Forget It |           |                        |
| Contact us form                         |           |                        |
| “Like” Reaction By Other Users          |           |                        |

<br>

[^ back to top ^](#Table-of-contents)
<br>


## Scope

To achieve user and owner’s goals, above are the minimum features to be included in this project. Also, **CRUD** Create, Read, Update, and Delete functions are required for this project so these are implemented as a part of the essential features.

- Simple design Home page where first-time users can recognise the purpose of the website easily. 
- Register page where users can create an account.
- Login page where users can log in to the website
- Logout function that users can log out the website
- Profile page 
- Search 
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely

> **Note:**<br>
> 

## Structure

### **Front end pages** 

The website consists of a **Home** page with **???? other core pages**.

- **Home** (`index.html`)<br>The landing page of the website. 

- **R** (`.html`)<br>

- **Product Detail** (`.html`)<br>

- **Register** (`account/signup.html`)<br>The page where users can create an account. Once a user creates an account successfully, they will be led to *Profile* page 

- **Login** (`account/login.html`)<br>The page where users who have an account can log in to the website. Once users log in successfully, they will be led to *Profile* page. Again the navigation bar is different to *Home* page, and once a user is logged in, the *profile* page and *logout* page is now visible on the navbar.
**Note:**<br>
> Please note that login is **case sensitive** 

- **Profile** (`profile.html`)<br>The page where users will be led when they create an account or log in. 

- **Search Results** (`search_results.html`)<br>

- **Delete Recipe** (`recipe_delete.html`)<br>

- **Delete Confirmation** (`recipe_delete_confirmation.html`)<br>The page where users get a confirmation message if they really wish to delete.

- **Page 404** (`page_404.html`)<br>The page that informs users, that the page they are looking for is not found and takes them back to *Home* page safely. 

<br>

[^ back to top ^](#Table-of-contents)
<br>


## Skeleton

It is a mobile-first website because people usually cook with a recipe so a good mobile-first design helps users whose main purpose is seeing recipes. For users whose main purpose is creating and posting recipes, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

### Wireframes

- [Wireframes: Home]()

- [Wireframes: #### ]()

- [Wireframes: Register]()

- [Wireframes: Login]()

- [Wireframes: Profile]()

- [Wireframes: Product Detail]()


## Surface

— **Colour** —

As this is a recipes website, I kept the colour scheme simple and clean as I wanted the main focus to be on the images.
<br>
The background 

— **Typography** —

* As a main font I used Lato, and as a backup font sans-serif
* On the logo text I used ...................
* On large headings I used ..................., and cursive as a backup font;
<br>

[^ back to top ^](#Table-of-contents)
<br>



# FEATURES

## Existing Features 
#### **Navigation menu displayed across all pages**

The navigation menu will help the user move easily across all pages.

The navigation buttons update depending on whether a user is logged in, and whether that user is the admin:

| Nav Link              |Not logged in  |Logged in as user
|:-------------         |:------------- |:------------- 
|Home                   |&#9989;        |&#9989;        
|#######                |&#9989;        |&#9989;        
|Register               |&#9989;        |&#10060;        
|Profile                |&#10060;       |&#9989;        
|Log Out                |&#10060;       |&#9989;             
|Log In                 |&#9989;        |&#10060;       


## Features to Implement in the future 
+ 
<br>

[^ back to top ^](#Table-of-contents)
<br>


# Database

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. 
Cloudinary is used for all images both by the superuser and a standard user for all images uploaded to the website.
<br>
The database contains three custom models - categories recipes and comments. The built in Django user model was utilized and each model linked to this. Each registered user is assigned a user id. They can add recipes which will be linked to their id, and each recipe has an auto generated slug field (this is derived from the recipe's title). The recipe can be edited and deleted by the person who added it or by admin. 

Below is the chart of the custom data model used.

![database](##################)<br>

###

# Technologies Used

- [Django3](https://www.djangoproject.com/) framework
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Postgressql](https://www.postgresql.org/) for the database
- [Bootstrap 5 ](https://mdbootstrap.com/) for the mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Cloudinary](https://cloudinary.com/) for images
- [Summernote](https://summernote.org/) editor for adding and editing the recipes
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website


## General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

## Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Tinypng](https://tinypng.com/) for resizing images
- [Tinypng](https://tinypng.com/) for resizing images
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

***

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](). 

# Deployment
## Heroku Deployment
This project was deployed through Heroku using the following steps:

### Step. 1 Installing Django and supporting libraries

Heroku needs to know which technologies are being used and any requirements, so the following commands were used in the Terminal in GitPod:
+ In the GitPod terminal, type ```pip3 install django gnuicorn``` to install django and gunicorn.
+ In the GitPod terminal, type ```pip3 install dj_database_url psycopg2``` to install the supporting libraries.
+ In the GitPod terminal, type ```pip3 install dj3-cloudinary-storage``` to install cloudinary libraries.
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ In the GitPod terminal, type ```django-admin startproject recipebook .``` to create your project. (Don't forget the .)
+ In the GitPod terminal, type ```python3 manage.py startapp the-lady-goldsmith``` to create your requirements file.
#### In settings.py file:
+ In the settings.py file type ```the-lady-goldsmith``` to create your requirements file.

### Step. 2 Deploying an app to Heroku
#### 2.1 Create the Heroku app:
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (lets_cook_it_app)
+ Select the appropriate region based on your location
+ Click 'Create App'
+ Add Database to App Resources - Located in the Resources Tab, Add-ons, search and add 'Heroku Postgres
+ Copy DATABASE_URL - Located in the settings Tab, in Config Vars, Copy Text

#### 2.2 Attach the Database:
#### In gitpod:
+ Create a new env.py file on the top level directory
#### In env.py file:
<br>

```
import os

os.environ["DATABASE_URL"] - "Paste in Heroku DATABASE_URL Link"
oos.environ["SECRET_KEY"] - "Make up a ramdom a randomSecretKey"
```

#### In heroku.com
+ Add Secret Key to Confid Vars

| Key                    | Value               |
| -------------          |:------------------- |
| SECRET_KEY             |*Secure secret key*  |
 
#### 2.3 Prepare our environment and settings.py file:
#### In settings.py:

+ Reference env.py

```
from pathlib import Path 
import os
import dj_database_url

if os.path.isfile("env.py"):
     import env

```
+ Remove the insecure secret key and replace - links to the secret key variable on Heroku

```
SECRET_KEY = os.environ.get('SECRET_KEY')

```

+ Replace DATABASES Section (comment out the old DataBases Section) - links to the DATABASE_URL variable on Heroku

```
DATABASES = {
     'default':
     dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

```
#### In the Terminal 
+ In the GitPod terminal, type ```python3 manage.py migrate``` to Make Migrations.

#### 2.4 Get our static and media files stored on Cloudinary:
#### In Cloudinary.com: 
+ Copy your CLOUDINARY_URL. eg. API Environment Variable copied from the Cloudinary Dashboard

#### In env.py: 
+ Add Clouldinary URL to env.py - be sure to paste in the correct section of the link

```
os.environ["CLOUDINARY_URL"] ="cloudinary://591333544891113:I7YqdHhfN01xRGjt55dcLywRks4@cloudmoira"

```

#### In Heroku.com:
+ Add Clouldinary URL to Heroku Config Vars - be sure to paste in the correct section of the link
+ Add DISABLE_COLLECTSTATIC to Heroku Config Vars **(temporary step for the moment, must be removed before deployment)**

| Key                    | Value               |
| -------------          |:------------------- |
| CLOUDINARY_URL         |cloudinary://5913333 |
| DATABASE_URL           |postgres://bxctnwwfx |
| SECRET_KEY             |*Secure secret key*  |
| DISABLE_COLLECTSTATIC  |1                    |

#### In settings.py:
+ Add Cloudinary Libraries to installed apps **(note: the order is important)**

```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',

```
+ Tell Django to use Cloudinary to store media and static files *Place under the static files*

```
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

```
+ Change the templates directory to TEMPLATES_DIR *Place within the TEMPLATES array*
+ Link file to the templates directory in Heroku *Placeunder the BASE_DIR line*

```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

```

+ Add Heroku Hostname to ALLOWED_HOSTS

```
ALLOWED_HOSTS = ["the-lady-goldsmith.herokuapp.com", "localhost"]

```

#### In Gitpod:
+ Create 3 new folders on the top level directory ```media, static, templates```
+ Create a Procfile on the top level directory also ```Procfile```

#### In the Procfile:
+ Add the following code ```web: gunicorn recipebook.wsgi```

#### In the Terminal 
+ Add ```git add .```
+ Commit ```git commit -m "Deployment Commit```
+ Push ```git push```

#### In Heroku.com:
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this
+ Underneath, locate 'Manual Deploy'; choose the main branch and click 'Deploy Branch'
+ Once the app is built (it may take a few minutes), click 'Open App' from the top of the page

<br>

## Forking the Repository
+ Log in to GitHub and locate the GitHub Repository
+ At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
+ You will have a copy of the original repository in your GitHub account.
+ You will now be able to make changes to the new version and keep the original safe. 

<br>

## Making a Local Clone
+ Log into GitHub.
+ Locate the repository.
+ Click the 'Code' dropdown above the file list.
+ Copy the URL for the repository.
+ Open Git Bash on your device.
+ Change the current working directory to the location where you want the cloned directory.
+ Type ```git clone``` in the CLI and then paste the URL you copied earlier.
+ Press Enter to create your local clone.

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Credits
### Code
* The Code Institute material was the main source of information used to create this project.
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [MND Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) was used as a general source of knowledge.
* [youtube](https://www.youtube.com/) 
* [Stack Overflow](https://stackoverflow.com/) 
* [Django docs](https://docs.djangoproject.com/en/3.2/) django documentation.
* [github docs](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) and (https://www.youtube.com/watch?v=3SKjPppM_DU) was used to create the 404 page.


### Media
* The Hero image and placeholder image were sourced from the following:
     * [](https://www.)
     * [](https://www.)
* The 404 page error image was sourced from the following:
     * [](https://www.)


### Acknowledgements
* I would like to thank the Slack Community for their endless support.
* I would like to thank Kasia Bogucka our class cohort facilitator for her constant assistance and encouragement.
* I would like to thank my husband for his understanding and support and for caring for our young children during the long hours taken to complete this project. 
* Finally, I would like to thank my mentor Adegbenga Adeye for his guidence and feedback throughout this project.
 
***