# Primal Silver Store

[![Build Status](https://travis-ci.org/SamuelWatson89/primal-silver-store.svg?branch=master)](https://travis-ci.org/SamuelWatson89/primal-silver-store)

This project is to set up an online store for Primal Silver, an independent silver jewelry maker. The business currently supplies is ware via an alternative online store, and would like to set up a more professional online shopping experience for its customers.
The online store will allow customers to view a full range of stock available for purchase, allowing customers to create and log into an account on the store site and make purchases online just like any other online store.

The site will allow user to shop by specific types of jewellery, and search for the right piece of silverware for them.

## UX

This, funcitonal but non trading, websites primary purpose is to allow the business to have a place to manage and display their stock online. The site will also allow customer to place and order and purchase the business stock. Giving the business and customer a single place to got to order bespoke jewellery, will assist in focused sales and trade.

As a business owner, i would need a place to display, sell and ship my items to customer with the most minimal effort and hassle.
As a business owner, i would need a somewhat of managing my stock level so i know what i have available to supply to customer.
As a customer, i want an online store where i can browse and purchase local hand crafted silver jewellery.

### User Stories

#### Business Owner

- I would like somewhere i can manage the sale and ditribution of my stock.

- I need to be able to manage the stock levels, so product are not over sold.

- I need to be able to allow customers to contact me with any concerns or queries.

- I need to have a log of all customer orders so I can ensure they are fulfilled.

- It would be hand to have some form of order tracking.

- An area depicting what my business does.

#### Customer

- As a customer i would like to be able to see a wide range of jewlellery at a quick glance

- As a customer i would like to make secure and safe purchases

- As a customer it would be nice to be able to create a wishlist to store items i like the look of incase of a sale in the future.

### Design, layout & wireframes

The main design was made by myself, but the bulk of inspiration was taken from [Patrol Base](https://www.patrolbase.co.uk/) (An online airsoft retail). 

I felt this has a good UI, an easy to follow e-commerce style design and easily navigatalbe.

I desided on a few bases colurs, earth greys and browns, with a promenant green to give a nature feel to the colouring.

I made use of [Figma](https://www.figma.com) to come plan the design, which can be [viewed here](https://www.figma.com/file/cxavKrJXKclzZyR0Qbz779/Primal-Silver-Store?node-id=0%3A1). As all things do, the design evolved over the course of the development.

## Features

### Features for the business

1. Stock management. A back end section to add and remove stock and monitor stock levels to accurately reflect what is readily available.

2. Ability to take payments.

3. Contact between customers and the business.

4. Visual display of products

5. Order tracking

### Features for the customer

1. Full stock list, paginated to 10 items per page.

2. Searchable stock

3. Ability to add an item to a wishlist

4. Secure storage for account information

5. User account section

Feature to add

1. Previous orders

## Technology Used

- [HTML](https://www.w3.org/html/)
  - Hyper Text Markup Language The main structure of the website, determining the placement and page elements.
- [CSS](https://www.w3.org/Style/CSS/)
  - Cascading Stlye Sheet, provide the websites struture with all its styling. From text sizes to background images. Using bootstrap provides a base for all these, and allow quick and easy creastion of styled site. I added my own styling to modify the look of a basic bootstrap website.
- [Javascript](https://www.javascript.com/)
  - This allows websites be more dynamic, allowing a developer to add annimations and movement to the pages.
  - This was used to make the message box swing out of view instead of just disappearing
  - The footer copyright year is kept uptodate with javascript also.
  - Each product type page as a dynamically displayed image dependants on the URL the user is on.
  - I have also made use of [Stripes](https://stripe.com/docs/js) javascript API to handle all payments.
- [jQuery](https://jquery.com/)
  - A library to make javascript simpler, this is bundled with Bootstrap to make some elements work.
- [Python](https://www.python.org/)
  - The focus of this project is aroiund this language, providing a backend to the projects, accessing the database and working with Django to handle the create of view, templates and security.
- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django provides a lot of fuinctionallity 'out of the box'. It was used to handle what the database will be structured, how the page will look and provide secure and ready to use user accounts.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL is a powerful, open source object-relational database system. It is well couple with Django projects, and this is why it was chosen
- [Heroku](https://www.heroku.com/home)
  - Heroku is a platform as a service based on a managed container system, with integrated data services and a powerful ecosystem, for deploying and running modern apps. This was chosen and its one of the most popular platofrms for hosting apps
- [AWS S3](https://aws.amazon.com/s3/)
  - S3 is cloud storage, where you can store and server static files for your websites dn applications. This is where all the CSS JS and Images are store for this project. S3 allowes for caching, so that the files are not need to be loaed each time a user vists.
- [Font Awesome](https://fontawesome.com/)
  - A great source for icons to be used on any website. Font awesome is one of the leaders in cross platorm compatible icon sets.
- [Google Fonts](https://fonts.google.com/)
  - I choose the fonts for the website form google fronts, [Rufina](https://fonts.google.com/specimen/Rufina?query=rufina), a Serif font for the titles. [Sintony](https://fonts.google.com/specimen/Sintony?query=Sintony) as a complimentry Sans-serif paragraph font. I used these font along with [Type Scale](https://type-scale.com/) to create a complementry typeface.

## Testing

The prjects does not have any automated testing implemented, i ran out of time to better learn and implement. All of the testing has been done by hand to ensure functionality. 

- The project aimed to make use of [Travis CI](https://travis-ci.org/) But as of yet i have had nothing but issues with getting it working once the project got underway. This is still to be worked on.

- A bug found and fixed was to do with the admin panel, and the way i had set up a product count context. This context was not the correct way to set it up, as when the databse was emptied of products, the whole application broke. This was not a great part of my day and had to rebuild the database!

- Responsivness was an issues, and has been worked on to get the site looking as good as pssible on mobile device. I made the error of building desktop first.

- The checkout page does not auto populate the logged in users address information if they update thier profile with it. This owuld be a nice feature to have added in, but i ran out of time to implement once i noticed it.

## Deployment

The project is deployed with Heroku Platform using the Gunicorn production server, ensuring there are no development tools or processes running on the live version of the app. Heroku will be used to update the build up form the master branch GitHub manually, ensuring that lastest updates are ready for users.

Heroku requires several Environmental Variables to function correctly.

- GMAIL_EMAIL (For the use of resetting passwords)
- GMAIL_PASSWORD (For the use of resetting passwords)
- SECRET_KEY (required for Django projects to function securly)
- STRIPE_PUBLISHABLE (Key for stripe checkouts)
- STRIPE_SECRET (Secret Key for stripe checkouts)
- DATABASE_URL (Link to the applications PostgreSQL database)
- AWS_ACCESS_KEY_ID (Access key to allow the transfer for files to AWS)
- AWS_SECRET_ACCESS_KEY (Secret key to ensure only the application is suppmitting files.)

The Postgres database is also hosted on Heroku.

All media and static files are host and served from AWS

### To run this projet locally

- Clone the Github repo using the green "Clone or download" button. and save it locally in your preferred location.

- Open the project in your editor of choice.

- Either use your prefered terminal, or if you editor has one built in, run the command in the root directory of the project
Windows: `python -m venv env`
Linux/max: `python3 -m venv env`
 env can be what ever you want the virtual encironment to be called.

- Run/Enter the virtual environment with the following terminal/shell commands/
Windows: `env\Scripts\Activate`
Posix/Linux/bash: `source env/bin/activate`
Remeember that `env` is what ever you named it when creating the environment.
- Once you have entered the env, you will need to install the dependencies the project requires.
In your terminal enter the following `pip install -r requirements.txt`
This should always be done inside a virtual environment to limit issue that may arise from globally installed packages.

- Set up environment variables. 
  - Rename the file `.env-dist` to just `.env`.
  - Acuquire and input the required keys and information.

- Once all this is done, you can run the application with the following command in the Virtual Environment Terminal
Windows: `python manage.py runserver`
Linux/mac `python3 manage.py runserver`

## Credits

### Content

All images and the identity are genorously supplied by [Primal Silver](https://www.facebook.com/Primal.silver/) Owned and operated by [Lewis Preston](https://www.facebook.com/lewis.preston.982)

### Code Assistance

Code Institute Slack channel when things did get dire, big thanks to all staff and students.

Many many many pages on [stack overflow](https://stackoverflow.com/)

[Code Entrepreneurs](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW) Django content on Youtube

[Brad Traversy](https://www.youtube.com/watch?v=e1IyzVyrLSU&t=37s) Django crash Course