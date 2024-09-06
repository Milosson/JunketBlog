# JunketBlog - Travelers Lifestyle. 🗺️ 

## Welcome to JunketBlog 
JunketBlog is a blog web app developed using the Django framework and other modern technologies. It forms a crucial part of my Portfolio Project 4 for Code Institute.
With that said..... let me tell you the story! ⬇️

## The story
The concept for this app initially started as a school project but soon took on personal meaning for me. I envisioned it as a space where my sister and mother could document and share their travel experiences. However, partway through the development and study process, my family experienced a significant tragedy that profoundly affected me. The emotional toll impacted my focus on this project and my studies overall, leading to delays and an extension for the submission deadline.

Before diving into the technical aspects, I want to extend my heartfelt thanks to Kieron and the team at Code Institute for their unwavering support during this challenging time.

Throughout these difficult months, I've learned a great deal - not only about coding but also about resilience and perseverance. While I regret that this submission doesn't reflect the level of engagement I had originally intended, it still represents the skills and dedication I've built over the past year.

## Transparency and Future Improvements
I am fully aware that certain aspects of this project are incomplete or not fully polished. Specifically:

* Automated Test Cases:  I was unable to implement robust automated testing in this iteration of the project. However, I manually tested all functions to ensure they work correctly, and the current version of the web app reflects those tests.
While I made efforts toward code quality, I recognize that my project does not fully comply with WC3 standards and PEP8 guidelines, which will be addressed in future updates. I have showcased compliance through screenshots of my largest Python files, but these changes have not been implemented yet to maintain a working app. This decision was made to avoid last-minute deployment issues while still showcasing the functionality of the application.
* General Engagement: Due to personal circumstances, my level of involvement in this project was impacted, and I wasn't able to deliver the engagement and depth I had originally planned.
That said, I plan to address these shortcomings and continue improving JunketBlog. My goal is to further develop this project, implementing the necessary improvements to make it a more robust and polished application.
* User Interface (UI) & User Experience (UX): The current UI and UX are not aligned with the level of design and usability I originally envisioned for the project. I plan to improve the visual design and overall user experience in future iterations.

<details>
  <summary><strong>PEP8 Compliance</strong></summary>

  Here are some images showing the PEP8 compliance checks that I plan to implement in my code:

  <strong>MODELS.PY</strong>
  ![PEP8 Compliance Models.py](https://i.imgur.com/cVxCK2R.jpeg)
  <strong>VIEWS.PY</strong>
  ![PEP8 Compliance Views.py](https://i.imgur.com/7ksp8jr.jpeg)
</details>

<details>
  <summary><strong>WC3 Validation</strong></summary>

  Here is a images showing the WC3 validation results:

  ![WC3 Validation Image](https://i.imgur.com/GVV7uMZ.jpeg)
</details>

You can view the live site here: [JunketBlog](https://junketblog-6cdd776f2302.herokuapp.com/) 
-  ### username: admin - pw: Admin123 (for login)

![Screenshot showcasing the responsive design of my web app](https://i.imgur.com/8tsWAJx.jpeg)


----
<details>
<summary>Table of Contents</summary>

- [JunketBlog - Travelers Lifestyle](#junketblog---travelers-lifestyle)
- [Welcome to JunketBlog](#welcome-to-junketblog)
- [The story](#the-story)
- [Transparency and Future Improvements](#transparency-and-future-improvements)
- [Agile Methodology](#agile-methodology)
- [Database Diagram](#database-diagram)
- [Wireframes](#wireframes)
- [Features](#features)
- [Features Left to Implement](#features-left-to-implement)
- [Admin panel](#admin-panel)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
- [Django Packages](#django-packages)
  - [Frameworks - Libraries - Software Used](#frameworks---libraries---software-used)
  - [Other Technologies Used](#other-technologies-used)
- [Bugs](#bugs)
  - [Known Issues](#known-issues)
  - [Resolved Issues](#resolved-issues)
- [Deployment](#deployment)
  - [Creating the Django Project](#creating-the-django-project)
  - [Create your Heroku app](#create-your-heroku-app)
  - [Set up Environment Variables](#set-up-environment-variables)
  - [Setting up settings.py](#setting-up-settingspy)
  - [Heroku Deployment](#heroku-deployment)
  - [Final Deployment](#final-deployment)
- [Code](#code)
- [Content and Media](#content-and-media)
- [Acknowledgements](#acknowledgements)
- [Special Thanks and Contributors](#special-thanks-and-contributors)

</details>


-----

## Agile Methodology

For this project, the Agile methodology was intended to guide development. GitHub and its Project Board were used to organize user stories and manage workflow. However, due to given circumstances and as a solo developer working on this project, I found myself focusing more on completing tasks within the given timeframe. User stories were initially created and directly added to the 'Done' column rather than progressively moving through 'To Do' and 'In Progress', as is typical in Agile workflows. I have also added the stories I would like to implement in the future to the 'Not Done' column.

While this approach deviated from a traditional Agile process, using user stories still helped ensure that key features were completed. I acknowledge that Agile methodology is particularly beneficial in a team setting, where collaboration and iterative feedback are essential. In future projects especially when working in a development team, I plan to adopt a more structured Agile approach with iterative development, regular testing, and proper backlog management to allow for greater flexibility and continuous improvement.


### User Stories - Find my GitHub Kanban Board [here](https://github.com/users/Milosson/projects/7/views/1)
<details><summary>User Story: Create a Travel Post (#1)</summary>

- As a **logged-in user**, I want to **create a new travel post**, so that I **can share my travel experiences with others.**

#### Acceptance Criteria:
1. A form is provided to input details such as title, featured image, content, location, travel date, and tags.
2. The post is saved as a draft immediately (As of now Admin needs to approve).
3. Upon successful creation, the user is redirected to the post list page.

</details>

<details><summary>User Story: Edit a Travel Post (#2)</summary>

- As a **logged-in user**, I want to **edit my existing travel post**, so that I **can update or correct the information.**

#### Acceptance Criteria:
1. The user can edit only their own posts.
2. A form pre-populated with the post's current data is provided.
3. Changes are saved and reflected on the post detail page.

</details>

<details><summary>User Story: View a List of Travel Posts (#3)</summary>

- As a **site visitor**, I want to **view a list of published travel posts**, so that I **can browse through different travel experiences.**

#### Acceptance Criteria:
1. The posts are paginated, showing a maximum of 6 posts per page.
2. Posts are displayed with title, featured image, excerpt, and travel date.
3. Users can navigate between pages.

</details>

<details><summary>User Story: View a Single Travel Post (#4)</summary>

- As a **site visitor**, I want to **view the details of a specific travel post**, so that I **can read the full content and comments.**

#### Acceptance Criteria:
1. The post is displayed with all its details, including title, content, featured image, location, travel date, and tags.
2. Approved comments are listed below the post.
3. A comment form is provided for logged-in users.

</details>

<details><summary>User Story: Add a Comment to a Travel Post (#5)</summary>

- As a **logged-in user**, I want to **add a comment to a travel post**, so that I **can share my thoughts or ask questions.**

#### Acceptance Criteria:
1. A form is provided to input the comment body.
2. Comments require approval before they are visible to others(Auto approval after 1 hour is added).
3. A success message is shown after submission, indicating the comment is awaiting approval.

</details>

<details><summary>User Story: Auto-Approve Comments (#6)</summary>

- As an **admin**, I want to **auto-approve comments submitted within the last hour**, so that **frequent commenters don't have to wait for manual approval.**

#### Acceptance Criteria:
1. Comments are auto-approved if they were created within the last hour and meet the approval conditions.

</details>

<details><summary>User Story: Edit a Comment (#7)</summary>

- As a **logged-in user**, I want to **edit my existing comment**, so that I **can correct or update my input.**

#### Acceptance Criteria:
1. The user can edit only their own comments.
2. A form pre-populated with the current comment data is provided.
3. The comment is updated after submission, and a success message is shown.

</details>

<details><summary>User Story: Delete a Comment (#8)</summary>

- As a **logged-in user**, I want to **delete my existing comment**, so that I **can remove it from the post.**

#### Acceptance Criteria:
1. The user can delete only their own comments.
2. Upon deletion, the comment is removed from the post, and a success message is displayed.

</details>

<details><summary>User Story: Submit a Contact Request (#9)</summary>

- As a **site visitor**, I want to **submit a contact request**, so that I **can reach out to the site owners with questions or feedback.**

#### Acceptance Criteria:
1. A form is provided to input the name, email, and message.
2. Upon submission, the request is saved, and the user is redirected to a success page.
3. An error message is shown if the form submission fails due to validation errors.

</details>

<details><summary>User Story: User Login (#10)</summary>

- As a **site visitor**, I want to **log in to my account**, so that I **can access features like commenting and post creation.**

#### Acceptance Criteria:
1. A login form is provided for users to input their username and password.
2. Upon successful login, the user is redirected to the home page or the page they were previously viewing.

</details>

<details><summary>User Story: Access Control (#11)</summary>

- As an **admin**, I want to **restrict access to certain features based on user authentication**, so that **only logged-in users can create posts or add comments.**

#### Acceptance Criteria:
1. Users must be logged in to access post creation, comment submission, comment editing, and comment deletion features.
2. Unauthorized users are redirected to the login page.

</details>

## Database Diagram

![ER Diagram](https://i.imgur.com/NTatVUj.jpeg)

## Wireframes

![](https://i.imgur.com/i11BvuO.png)

## Features

<details>
  <summary><strong>User Authentication</strong></summary>

  - **Login:** A login page allowing users to sign in and access protected features such as creating, editing, or commenting on travel posts. Login protection is applied to pages that require the user to be logged in.
  - **Authorization:** Restricted access to certain functionalities like commenting or editing for non-authenticated users.
</details>

<details>
  <summary><strong>Travel Post Management</strong></summary>

  - **Create Travel Post:** Logged-in users can create new travel posts through a form that supports image upload, travel date, location, and tags.
  - **Edit Travel Post:** Users can edit their travel posts and update information such as title, content, location, and tags.
  - **Post Slug:** Each travel post generates a unique slug for user-friendly URLs.
</details>

<details>
  <summary><strong>Post List & Pagination</strong></summary>

  - **Post List Page:** All published travel posts are listed on an index page, showing 6 posts per page.
  - **Pagination:** Users can navigate through multiple pages of posts via pagination.
</details>

<details>
  <summary><strong>Post Detail View</strong></summary>

  - **Post Detail Page:** Each travel post has a detail page showing the full content, including title, image, location, and publish date.
  - **Related Comments:** Comments related to a specific post are displayed below the post.
</details>

<details>
  <summary><strong>Commenting System</strong></summary>

  - **Add Comment:** Logged-in users can add comments to posts, which may include a body of text and optional tags.
  - **Auto-approval:** Comments that are older than one hour are automatically approved.
  - **Edit Comment:** Users can edit their own comments.
  - **Delete Comment:** Users can delete their own comments. Non-authors are restricted from deleting others’ comments.
</details>

<details>
  <summary><strong>Contact Us Form</strong></summary>

  - **Contact Form:** A contact form page where users can send messages to the site owner. The form includes fields for name, email, and message.
  - **Form Validation:** Users are notified of errors such as missing fields and prompted to correct them before submission.
</details>

<details>
  <summary><strong>Post and Comment Tagging</strong></summary>

  - **Post Tags:** Travel posts can be tagged with various keywords for better categorization and searchability.
  - **Comment Tags:** Users can optionally tag their comments to associate them with related topics.
</details>

<details>
  <summary><strong>Cloudinary Integration for Image Uploads</strong></summary>

  - **Image Uploads:** Users can upload images for their posts, which are stored on Cloudinary.
  - **Cloudinary Storage:** Post images are fetched directly from Cloudinary and displayed on each post’s detail page.
</details>

<details>
  <summary><strong>Message Feedback System</strong></summary>

  - **Success & Error Messages:** Users receive feedback via Django’s messages framework, such as confirmations that comments or posts were saved, or warnings for submission failures or insufficient permissions.
</details>

<details>
  <summary><strong>Dynamic Slug Generation</strong></summary>

  - **Unique Slug Creation:** Each travel post generates a unique slug based on the title, ensuring unique and SEO-friendly URLs.
</details>

<details>
  <summary><strong>Approval Workflow for Comments</strong></summary>

  - **Admin Approval:** Comments can either be manually approved or auto-approved if they meet certain conditions, such as being posted more than an hour ago.
</details>

<details>
  <summary><strong>Success Page for Contact Form Submission</strong></summary>

  - **Contact Success:** After successful submission of the contact form, users are redirected to a success page confirming the message was sent.
</details>

## Features Left to Implement

<details>
  <summary><strong>Search Fields</strong></summary>

  - **Implementation of Search Functionality:** Introduce search fields to allow users to find travel blogs, tags, and usernames quickly and efficiently.
</details>

<details>
  <summary><strong>Delete Functionality for Travel Posts</strong></summary>

  - **Add Delete Option:** Implement a delete option for travel posts to allow users to remove their own posts as needed.
</details>

<details>
  <summary><strong>Tag Logic Enhancement</strong></summary>

  - **Improved Tag Management:** Refine the tagging system to add logic that enhances its usefulness, such as filtering or displaying related posts.
</details>

<details>
  <summary><strong>UI/UX Improvements</strong></summary>

  - **Overall Design Enhancements:** Work on improving the overall user interface and user experience for better navigation and aesthetics.
</details>

<details>
  <summary><strong>Navbar Options Expansion</strong></summary>

  - **Additional Navbar Features:** Add more navigation options for users to search for travel blogs, tags, usernames, etc.
</details>

<details>
  <summary><strong>Framework and Event Listener Integration</strong></summary>

  - **Adding Frameworks:** Incorporate additional frameworks and design elements to enhance functionality and interactivity.
</details>

<details>
  <summary><strong>Comment Approval Checker</strong></summary>

  - **Create a Comment Checker:** Develop a function to review comments before they are auto-approved, ensuring quality and relevance.
</details>

<details>
  <summary><strong>Travel Post Approval Functionality</strong></summary>

  - **Post Approval Workflow:** Add a function for a review process for travel posts before they are published, ensuring content quality.
</details>



## Admin panel

<strong> Admin Interface Description </strong>

The admin interface of the content management system is designed to provide a comprehensive and user-friendly experience for managing various aspects of your website. Below is a detailed description of its key sections and functionalities:

<details>
  <summary><strong>INTERFACE PREVIEW</strong></summary>
  <img src="https://i.imgur.com/xoanVGq.jpeg" alt="Django Interface" />
</details>

<details>
  <summary><strong>Site Administration</strong></summary>

  - **Accounts:** Manage user accounts, including adding new users and modifying existing ones.
  - **Email Addresses:** Oversee and update email addresses associated with user accounts.
</details>

<details>
  <summary><strong>Authentication and Authorization</strong></summary>

  - **Users:** Add, edit, and manage user profiles and permissions.
  - **Groups:** Organize users into groups for easier management of permissions and roles.
</details>

<details>
  <summary><strong>Blog Management</strong></summary>

  - **Travel Posts:** Create, edit, and delete blog posts related to travel. This section includes fields for title, content, author, and publication date.
  - **Comments:** Moderate comments left by users on blog posts. You can approve, edit, or delete comments.
  - **Tags:** Manage tags used to categorize blog posts. Add new tags or edit existing ones.
</details>

<details>
  <summary><strong>Contact Requests</strong></summary>

  - **Contact Requests:** View and respond to contact requests submitted through your website’s contact form.
</details>

<details>
  <summary><strong>Attachments</strong></summary>

  - **Attachments:** Manage files and media uploaded to your website. This includes adding new files and organizing existing ones.
</details>

<details>
  <summary><strong>Recent Actions</strong></summary>

  - **Recent Actions:** A log of the most recent activities performed in the admin interface, such as edits and additions to blog posts, tags, and comments.
</details>

--- 
## Technologies Used

#### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)- was utilized in this project to structure the web pages in a semantically meaningful way, prioritizing better accessibility.
* [CSS3](https://en.wikipedia.org/wiki/CSS)- was used in this project to leverage its advanced styling capabilities and enhance the visual appearance of the website.
* [JavaScript](https://www.javascript.com/)- in this project, JavaScript code is kept minimal. It is primarily utilized to automatically hide alert messages after 3 seconds and display a "Move to Top" button upon scrolling.
* [Python](https://www.python.org/)- was utilized to create database models, create all the views for web app funcionality, create forms used throughout the website, connect URL paths and install necessary dependencies specified in the requirements.txt file for the successful execution of this project. Python will be used to write automated tests as well.

## Django Packages

<details>
  <summary><strong>Packages</strong></summary>

  * [Gunicorn](https://gunicorn.org/) - was utilized as the server to deploy the Django web application in a production environment, specifically Heroku.
  * [Dj Database URL](https://pypi.org/project/dj-database-url/) - to parse the database URL from the environment variables in Heroku.
  * [Psycopg2](https://pypi.org/project/psycopg2/) - used as an adapter for Python and PostgreSQL databases.
  * [Summernote](https://summernote.org/) - as a text editor in some Django fields.
  * [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - used for authentication, registration, and account management.
  * [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - was used for easy rendering of Django forms with customizable templates and layout controls.
</details>

### Frameworks - Libraries - Software Used

<details>
  <summary><strong>Frameworks and Libraries</strong></summary>

  * [Django](https://www.djangoproject.com/) - was used as the framework that provides the necessary tools and functionalities for building full-stack web applications. Django enables rapid and secure development.
  * [Bootstrap](https://getbootstrap.com/) - used to style the website through its classes, add responsiveness and interactivity, and use ready components.
  * [Cloudinary](https://cloudinary.com/) - was used to host the static files and media files for the website and use them in the production environment, Heroku.
  * [Git](https://git-scm.com/) - used for version control by utilizing the Gitpod terminal to commit code to Git and push to GitHub.
  * [GitPod](https://www.gitpod.io/) - used as an IDE workspace to write code for this project.
  * [GitHub](https://github.com/) - used to store the project's code after being pushed from Git version control and to create Issues & Project Kanban.
  * [Heroku](https://id.heroku.com) - used to deploy the web application in a production environment.
  * [CI-DBS PostgreSQL](https://dbs.ci-dbs.net/) - database used through Heroku.
  * [Smartdraw](https://www.smartdraw.com/) - to set up a simple wireframe and draw th ERD.
  * [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - was used to inspect page elements, debug, troubleshoot, and test features and adjust property values. Using the Lighthouse extension installed in the Chrome Browser, the performance report was generated but not displayed in my readme, total results: 91.
</details>

### Other Technologies Used

<details>
  <summary><strong>Other Technologies</strong></summary>

  * [Fontawesome](https://fontawesome.com/) - used to get icons used in the website.
  * [Favicon.io](https://favicon.io/) - used to generate favicon.
</details>


---

# Bugs

#### Known Issues

1. **Image Upload Errors**  
   **Status**: **Unsolved**  
   **Description**: Users occasionally experience issues when uploading images, resulting in an error message. This may be due to file size limitations or unsupported formats.  
   **Workaround**: Ensure that the image is under the specified size limit (e.g., 5 MB) and in a supported format (e.g., JPEG, PNG).


3. **Mobile Responsiveness Issues**  
   **Status**: **Unsolved**  
   **Description**: Some elements may not display correctly on certain mobile devices, particularly in landscape orientation.  
   **Workaround**: Users are encouraged to check the blog on different devices and report any inconsistencies.

#### Resolved Issues

1. **Login Redirect Loop**  
   **Status**: **Solved**  
   **Description**: Some users experienced a redirect loop upon logging in, preventing access to their account.  
   **Solution**: This issue was resolved by adjusting session handling in the authentication middleware.

2. **Post Creation Fails**  
   **Status**: **Solved**  
   **Description**: A bug causing post creation to fail without a clear error message was fixed.  
   **Solution**: Improved validation checks were added to ensure all required fields are filled before submission.

# Deployment

## Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project: `django-admin startproject <your_project_name>.`
* Create app: `python manage.py startapp <your_app_name>`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display Django project - The install worked successfully! Congratulations!

## Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1` (note: this must be either removed or set to 0 for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.

## Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

## Setting up settings.py
* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku, click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: 
```ALLOWED_HOSTS = ['<Heroku_app_name>.herokuapp.com', 'localhost']```
* Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Commit and push the code to the GitHub Repository.

## Heroku Deployment 
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

## Final Deployment

* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

----


## Code
- The basic set up of the website was done by strictly following the steps as described in Code Institue Full Stack Frameworks module - Django walkthrough project `"I Think Therefore I Blog"`. As well this project was used along development for clarifying questions or problems raised during development stage.
- Comment model was used same as in Django walkthrough project `"I Think Therefore I Blog"` for ease of building the project.
- After encountering errors, snipets of codes were taken from [Django Documentation ](https://docs.djangoproject.com/en/4.2/) after reading it and finding the right solutions. (A lot of help from friends and my father as well)
- In order to add min and max length to username field in SignUp form was used this code [Stack overflow ](https://stackoverflow.com/questions/50548685/how-to-add-max-length-to-allauth-username).

## Information Sources / Resources
- Code Institutes Full Stack Framework Module, mainly the 'blog' walkthrough project.
- Youtube videos by [CodeWithStein](https://www.youtube.com/watch?v=I8TRkEcw9Mg) - [Codemy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - [Django Documentation](https://docs.djangoproject.com/en/4.2/) to better understand Django MVT framework.
- [Google](https://www.google.com/) as a research tool.
- [Create a Simple Django Blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) used as an instructor how to create a Django Blog webapp.
- [django-allauth](https://builtwithdjango.com/blog/styling-authentication-pages) how to style authentication fields.

## Content and Media

The images used in this project are primarily sourced from Pixabay, Unsplash, and Pexels. These platforms offer a wide range of high-quality, royalty-free images that can be used without the need for attribution.

<details>
  <summary><strong>Image Sources</strong></summary>

  - **Pixabay:** A repository of over 1.7 million free stock photos, videos, and music that can be downloaded and used for personal and commercial purposes.
  - **Unsplash:** A collection of freely usable images contributed by photographers from around the world, allowing users to download and utilize images without attribution.
  - **Pexels:** A platform providing free stock photos and videos, which can be used freely for both personal and commercial projects.

</details>

<details>
  <summary><strong>Future Steps</strong></summary>

  - **Quality Assurance:** I will continue to curate high-quality images from these sources to enhance the visual appeal of the content.
  - **User Contribution:** I plan to encourage users to submit their own images, promoting a community-driven approach to content creation.

</details>

By utilizing these resources, I ensure that my webapp remains visually engaging while adhering to copyright and licensing guidelines.



## Acknowledgements

I want to take a moment to express my heartfelt gratitude to **Code Institute** and especially **Kieron** for his unwavering support during what has been a challenging period in my life. His understanding and approval for an extension, given my personal circumstances and the tragic events my family faced, have been truly invaluable.

Although I couldn't fully utilize the extra time and find myself feeling a bit disappointed that this submission doesn't reflect my true potential, I recognize the immense knowledge and skills I’ve gained throughout this wonderful year with CI. My goal is to submit what I have now and await the assessment so I can roll up my sleeves and polish this app into something I can be proud of. I'm excited about the journey ahead and eager to bring this project to its true potential!

## Special Thanks and Contributors

**💙 Kieron** - Unwavering support  
**💖 Code Institute** - Guidance and encouragement  
**💙 Tove** - Loving support  
**💖 Haitem** - Technical support and motivation  
**💙 My Family** - Unconditional support and love  
**💖 Julia** - Motivational support  
**💙 Leona** - Motivational support and guidance in life and projects  
**💖 Samson** - Encouraging voice lines over Discord and a positive vibe at all times


