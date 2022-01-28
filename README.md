# The Lady Goldsmith
## **Code Institute - Portfolio Project 5: _E-commerce Application_** 
The Lady Goldsmith! is an online e-commerce fine jewellery store.

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes.
## Demo

**View the Live Website [Here](https://ecommerce-pp5.herokuapp.com/)**
<br>
<img src="https://github.com/moirahartigan/the-lady-goldsmith/blob/main/readme/responsiveness/responsiveness.png">


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
+ [APIs and configuration](#APIs-and-configuration)
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
<br>

# APIs and configuration

The project also uses a number of API's and configuration, below are the steps to configure the API in your environment

## Google emails

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>
<br>![App password](readme/misc/gmail_app_passwords.png)
4. Click create and a 16 digit password will be generated, note the password down
5. Go to heroku app config vars and set

     | Key                    | Value               |
     | -------------          |:------------------- |
     | EMAIL_HOST_PASS           |*paste in password*  |
     | EMAIL_HOST_USER           |*the email used above*  |

7. Set and confirm the following values in the settings.py file to successfully send emails
<br>
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>
<br>![API keys](readme/misc/stripe_keys.png)
<br>
4. Note the values for the publishable and secret keys
5. In heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br>
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://ecommerce-pp5.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>
<br>![Webhook](readme/misc/webhook.png)
<br>
9. Note the key created for this webhook
10. In heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

# Deployment
There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "ecommerce-pp5"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](readme/misc/aws_s3_static.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](readme/misc/aws_cors.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](readme/misc/aws_bucket.png)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "ecommerce-pp5"
12. Add the "AmazonS3FullAccess" policy permission for the user group
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::ecommerce-pp5",</code>
<br><code>"arn:aws:s3:::ecommerce-pp5/*"</code>
<br><code>]</code>
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](readme/misc/aws_policy.png)
18. Go to Users and create a new user
19. Add the user to the user group ecommerce-pp5
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
<br>![AWS Bucket Policy](readme/misc/aws_users.png)
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](readme/misc/aws_settings_gitpod.PNG)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 


## Heroku Deployment
This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ Create your Procfile and insert the following code: ```web: gunicorn ARTstop.wsgi:application``` and make sure there is no additional blank line after it. 
+ Push these files to your repository.

### Creating Heroku App
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropriate region based on your location
+ Click 'Create App'

### Connecting to GitHub
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this.

### Environment Variables
+ Click the 'Settings' tab towards the top of the page
+ Locate the 'Config Vars' and click 'Reveal Config Vars'
+ The following variables all need to be added:

|Variable name         |Value/where to find value                                |
| ---------------------|---------------------------------------------------------|
|AWS_ACCESS_KEY_ID     |AWS CSV file(instuctions above)                          |
|AWS_SECRET_ACCESS_KEY |AWS CSV file(instuctions above)                          |
|DATABASE_URL          |Postgres generated (instructions above)                  |
|EMAIL_HOST_PASS       |Password from email client                               |
|EMAIL_HOST_USER       |Site's email address                                     |
|SECRET_KEY            |Random key generated online                              |
|STRIPE_PUBLIC_KEY     |Stripe Dashboard > Developers tab > API Keys > Publishable key |
|STRIPE_SECRET_KEY     |Stripe Dashboard > Developers tab > API Keys > Secret key |
|STRIPE_WH_SECRET      |Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
|USE_AWS               |True (when AWS set up - instructions below)              |


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