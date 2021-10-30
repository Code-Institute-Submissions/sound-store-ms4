# Sound Store


# UX
## User Stories:
The target audience for Sound Store is both anyone looking for musical instruments, and musicians who also want to read the sites blog which is intended to impart insight into musical topics. 
1. I want to find what I am looking for in an intuitive, easy manner and to not have to go to too much effort to find what I need.
2. I want relevant information on products I am querying. This includes price, a product image, details of free delivery.
3. I want a way to choose quantities of anything I want and update these quantities and/or delete a product from my shopping cart.
4. I want to be able to checkout when I have chosen my purchases.
5. I want to be able to save my contact details when I checkout so that I do not need to enter them during future purchases.
6. I want to see my purchase history in my profile, which also stores my contact details.
7. I want to be able to logout of my profile.
8. As well as have easy access to products via links on screen, I also want to be able to search for my own search terms.
9. To be able to navigate pages intuitively via button links without recourse to the browser back and forward arrows.
10. To have access to a blog to get musical information not necessarily linked to the store.
11. To be able to contact the store via a contact form.


# Technologies Used:
1. Html, Css, JavaScript and Python are the programming languages used.
2. Django - A Python framework, was used to build the site.
3. Jquery - A simpler form of javascript.
4. Bootstrap - A css framework.
5. Favicon (https://favicon.io/favicon-generator/) - To get the icon for the sites tab.
6. Font Awesome (https://fontawesome.com/v4.7/icons/) - To get icons for social media / shopping cart etc.
7. Google Fonts - (https://fonts.google.com/) - To get fonts for the site.
8. Balsamiq - Used to make wireframes.
9. Stripe - Used to process payments in the store
10. PostgreSQL - Heroku database used on the deployed site.
11. SQlite3 - Django database used during development.
12. Github - Used to store my project.
13. Coolors (https://coolors.co/) - To generate a colour pallette for the sites styling.
14. Temp Mail (https://tempmail.net/) - Used to generate a temporary email account to test that emails are being sent correctly.
15. Gmail - Used for 2-step authentication when registering for an account. 


# Design
My goal in designing the site was to create a site that was welcoming to everybody. The way I tried to achieve this was to make the design as uncluttered as possible. I had in mind always the idea of a non-musician buying a gift for somebody and the buyer needing to be able to navigate the site as easily as possible. This would require a clear layout and many easy to find links to the products.

## Colours Used
With the exception of the White and Gold colours, the rest of the colours came from the Coolors app (https://coolors.co/). This app chooses a palette of five complimentary colours that work well together. Additionaly I could choose an extra five shades of blue to add to the palette. colour no.1 was used as the main text colour of the site. The lighter shades of blue were used for text hover effects mainly. 

1. Dark navy - #011627 (Main text colour of the site)
2. White - #fdfffc
3. Light green - #2EC4B6 (Admin edit button)
4. Red - #e71d36 (Admin delete button and in place of bootstrap danger class)
5. Orange - #ff9f1c 
6. Dark blue - #122c34
7. #224870 Lighter shade of blue than no.6
8. #36597D Lighter shade of blue than no.7
9. #4A698A Lighter shade of blue than no.8
10. White
11. Gold (Rating star)

## Fonts Used
1. Sonsie One - This font reminds me of some of the Fender guitars or Gibson guitars logos and therefore I thought it would be a good fit for a music related site.
2. Roboto - Easy to read font used in the navbar links
3. Tenor Sans - A readable font to render the product names and page headers in.

## Images
The site relies heavily on images. The home page uses a carousel of three images. These three images are used to represent the actual walk-in store. On the index page are clickable instrument-image links to the product categories. Also there are a large number of product images on the site.













# Testing
During development of the site Debug was set to True in the project level settings.py file. This provided me with django error screens when there were issues with my code. During deployment this was set to False and replaced with custom error screens. 

All testing of the site was conducted on both the deployed Heroku site and during development on the Gitpod server.

## Manual Testing Of Each Section Of The Site
### BASE.HTML
base.html consists of the sites navbar with various page navigating links and the sites footer with social media links, the link to the contact app and to the blog, aswell as the copyright notice. When testing this page, I first of all checked all links on mobile view to make sure they matched the desktop view in their functionality, which they did. The main design difference between both is that on mobile there is a 'burger bar' icon leading to the navigation links in a dropdown menu. The search bar, profile link and shopping cart link all perform the same function as in the desktop view. Also the 'sound store' homepage link is not present in the mobile view but the home link in the dropdown menu performs the same function as it. 
#### Testing of each feature
1. The 'sound store' link brings me back to the homepage.
2. The searchbar allows me to search the site with my own terms. I tested this by typing 'bass' into it and a products page with all bass guitar listings renders.
3. The 'My Account' icon opens up a dropdown menu. If I am signed out this reads 'Login' and 'Register'. If signed in as a non-superuser this reads 'My Profile' and 'Logout'. When signed in as a superuser this reads 'Product Management', 'Upload Blog', 'Customer Messages', 'My Profile' and 'Logout'. All links lead to their respective pages, 'Product Management' being a page for uploading products to the database.
4. The shopping cart icon brings me to the shopping cart page. If this page is empty, a €0.00 will be present underneath the icon. If the cart has items in it, the subtotal of all items will be present underneath the icon. 
5. Each navigation link except home, which just renders the index.html template, opens a dropdown menu. 























# Bugs Encountered
### Webhooks bugs
1. When attempting to send webhook test events, I was receiving a result of "Test webhook error:401". This was fixed by opening up the ports tab in Gitpod and making the 8000 port public.
2. On another occasion while trying to send a test webhook, I was receiving a result of "Test webhook error:404". This was fixed by updating the region code, i.e. "...eu(number)..." in the gitpod workspace url. This number appeared to change somewhat regularly and so needed to be updated in the stripe endpoint url in the stripe dashboard. 
3. Due to the superuser being created at the beginning of development before the profiles app was created, the profiles app did not recognise the superuser name and threw an error 404 screen in response to my attempting to login to admin. This was fixed by commenting out the 'if created:' statement in the profiles.models file... {show picture} ... , logging in with the superuser name and password, and then uncommenting the code. On both the commenting and uncommenting of the 'if' statement, the line inside was indented appropriately in order for the code to work.

### Product Admin Bugs
1. When Testing the admin-only add product form in add_product.html, I successfully added numerous products to the store. I then deleted these products in the admin database. The result of this was that my site become totally unusable. When loading my site using 'python3 manage.py runserver' I was getting a 404 error saying that my home page was not found. I tried undoing all the work I had done leading to this error and redoing it but it did not fix the issue. Finally I found a post on Slack related to this and realised that the products deleted from my database were in my shopping cart at the time and thus were cached in the entire project. I deleted the sessionid from developer tools and this fixed the error. 

### Deployment bugs
1. When trying to load my db.json file to my postgres account I was encountering this result in the console. // Show picture here. To fix this I used a json formatter to make the file easier to read and then with advice from slack I identified where in the file a full country name was used instead of a two letter name which the installed 'CountryField' requires. I opened up my db.json file, found these full country names and changed them to two letter names instead and this fixed the issue.
2. Again when trying to upload this db.json file I received this message // Show picture here. A suggestion seen on Slack suggested to upload the json file without any user information. So I identified, again using the json formatter, where this data was and deleted it. I then uploaded this file to postgres using 'python3 manage.py loaddata db.json' and the products and categories showed up in the site as expected.
3. When trying to push to Heroku, I was getting an error due to my requirements.txt file including psycopg-binary==3.0.1. While I had installed psycopg2-binary==2.9.1, I hadn't installed the former and am not certain how it got in to my project. I deleted it from the requirements.txt file and the project pushed successfully to heroku.
4. While trying to git push my media and static files to heroku I was getting a 'Push Failed' status which had the following code 'Error while running '$ python manage.py collectstatic --noinput''. In order to fix this I tried re-writing the code in my settings.py file to make sure it was correct. After some attempts with this I realised that my 'AWS_STORAGE_BUCKET_NAME' variable in settings.py was set to the wrong name. After fixing this the push to heroku was successful.
5. After setting up my AWS S3 bucket and uploading my images to it, the images that were not also in my database and were linked to in image file paths in my code were not showing on my deployed heroku page. After going back through course material to ensure I had set up my S3 bucket correctly I finally tried something that I had seen others do on Slack. That is I put a link to the settings.py variable that links to my AWS account into the file paths on my index.html page. I put for example '{{ MEDIA_URL }}drums-category-1.jpg' in and this worked to render the images correctly on the deployed site.
6. On one occasion after pushing to my heroku app, I began receiving the message pictured below on my deployed site. This was fixed by opening up my project in Firefox and working on it there for the rest of development, as opposed to Duck Duck Go which I had been using before that. // Insert image here

### Blog bugs
1. When trying to link to the blog in the base.html page, I was repeatedly getting an error. After trying a few things I changed the name of the blog view from 'BlogPostPage' to 'blog_post_page' and this fixed the issue.

# Deployment
## Deployment to Github
1. First I created my project repository using the Code Institute template.
2. From there I clicked on the green Gitpod button that brought me to the editor. This is the last time I accessed the project in this way, from there on I accessed it through going to gitpod.io/workspaces and clicking the dropdown on the right of the listing and pinning my project. This means that all of my installed packages will not need to be re-installed with each opening of the workspace. I would then click on the title to access the project. 
3. When I was ready to commit an update of my work to github I typed into the command line interface, 'git add .', then 'git commit -m "Commit message", followed by 'git push' to push the update to the repository.

### To Clone this Project
1. On my github page, https://github.com/aaronh1986/Irish-Music-Vault, click on the button titled 'Code' to the left of the green button for accessing the editor.
2. Click the button with the clipboard icon to copy the url. 
3. Within the terminal of the editor, type git clone followed by copying in the url that you copied and press enter to create a clone of the project. You will need to change the current working directory to the location that you want to create the cloned project within.

## Deployment to Heroku
1. First I logged into my Heroku account, then clicked on the button in the top right of the screen with 'NEW' on it followed by 'Create New App'. I then titled my project 'ms-4-sound-store' and chose the region nearest mine.
2. In the resources tab within the dashboard, I clicked on add-ons and provisioned Heroku Postgres. Then within my Gitpod terminal, I typed in 'pip3 install dj_database_url' which Django needs to connect to the Postgres database on Heroku. This command parses a database url that Heroku created and allows connection to it. I also installed a package with 'pip3 install psycopg2-binary' which django needs. I froze both of these requirements with 'pip3 freeze > requirements.txt'.
3. I then backed up my database into a db.json file by running 'python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json'.
4. On the project level settings.py file, I imported dj_database_url at the top of the file. I then commented out the DATABASES variable after copying it and changed the 'default' database configuration key to 'dj_database_url.parse('put DATABASE_URL in here taken from Heroku config variables')'. 
5. I then ran migrations to the postgres database by typing 'python3 manage.py loaddata db.json' which loaded my db.json file to the new database. 
6. (See Bugs Encountered, Deployment section, numbers 1 + 2 ). After deleting all of the user data in the new database, I created a new superuser with 'python3 manage.py createsuperuser' (name = admin, password = gtnwhnks ).
7. I then set up an 'if' statement in my settings.py file so that while my project is connected to Heroku it will parse the DATABASE_URL enviornment variable that is stored in my account in order to run the database. Otherwise it will connect to my sqlite3 database if it cannot find this configuration variable.
8. I then installed gunicorn by typing 'pip3 install gunicorn' and froze this requirement. Gunicorn works as the webserver for the project.
9. I then created a Procfile. This was used to create a web dyno with heroku and run gunicorn in order to serve the django project.
10. So that heroku would not collect static files upon deployment (as I was using AWS for this) I typed 'heroku config:set DISABLE_COLLECTSTATIC=1'. I also put the name of my heroku app into to the ALLOWED_HOSTS variable in settings.py. 
11. I then git added, commited and pushed to github, and deployed to Heroku with 'git push heroku main'. 
12. Then to ensure automatic deployment to Heroku when pushing to Github I went to my Heroku dashboard and on the Deploy tab clicked on the Github option in the Deployment Method section, and connected to my Github repository in the Connect to Github section below that. Then in the Automatic Deploys section, I clicked on Enable Automatic Deploys.
13. I then went to https://miniwebtool.com/django-secret-key-generator/, to generate a secret key for my django app and put this in the Config Vars section of my Heroku app, removing it from settings.py and replacing with 'SECRET_KEY = os.environ.get('SECRET_KEY', '')'.
14. When trying to create a new app in the terminal, I was getting an error stating "raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.") django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.". Since I had put my SECRET_KEY variable into Heroku config vars, gitpod could not find the value for working locally. I first put the value into the enviornment on my gitpod.io/workspaces account. That did not seem to work even after refreshing the workspace. After that I decided to create an env.py file and put the value in there. That fixed the problem.

## Deployment to S3 on Amazon Web Services
Amazon Web Services S3 was used to store the projects static files and images.

1. On 'aws.amazon.com' I set up an account following the onscreen instructions after clicking the orange button in the top right corner of the homepage. 
2. Once logged in I clicked on s3 and pressed the orange button with Create Bucket on it.
3. On the following page I unblocked public access.
4. I then enabled Static Website Hosting.
5. In the permissions tab, within the CORS configuration link I filled in the text area with code that connects the heroku app to the s3 bucket.
6. Within the Bucket Policy tab I clicked on Generate Policy to generate my policy and then copied the policy into the text area of the Bucket Policy Tab on the previous page. 
7. In the Access Control List tab, within the Public Access section I activated List Objects for Everyone.
8. To create a user for accessing my s3 bucket I clicked on IAM (Identity & Access Management) in the services section of my aws dashboard. 
9. Firstly I created a group to which to give access to my s3 policy. And then I created a user which was part of that group.
10. To create the group. I clicked on groups in the menu and clicked on the blue Create New Group button, giving my group the name manage-sound-store.
11. Next I created a policy by clicking on the link for it in the dashboard and clicking on the Create Policy button. In the JSON tab I clicked on Import Managed Policy and searched and chose the 'Amazons3FullAccess' policy and clicked the Import button. To limit access to just my s3 bucket, I used the s3 bucket ARN number and pasted it into the resources key on the Create Policy page. Clicking on the Review Policy I gave it a name and clicked Create Policy. 
12. Clicking on the group that I created in the groups tab, I then attached the policy to my group but clicking on the Attach Policy button and searching for my group name to attach it to.
13. I then created a User for access to the group. I clicked on Users in the dashboard and created a user named sound-store-staticfiles-user, clicking on the Programmatic Access box.
14. I then clicked the box next to my group's name and pressed next page until I came to a button titled Create User.
15. This gave me access to a CSV file giving me access to the users Access Key and Secret Access Key which were necessary to link between the s3 bucket and my django project.   
16. To connect Django to the s3 bucket, I installed two packages, boto3 and django-storages using the command for installing packages, 'pip3 install (package name)' and froze these requirements. I added 'storages' to the installed apps section of my readme.
17. I put my AWS Access Key and Aws Secret Access Key into my settings.py file and put the actual values for these in my Heroku app config variables so that they do not get pushed to Github and therefore exposed.
18. In settings.py I inserted my bucket name, region name, access to both aforementioned keys from Heroku config variables and a link to the s3 bucket domain name where my static files are kept.
19. I then created a file named custom_storages.py, which will be used to connect django to the AWS s3 account for uploading static files and media images. I then linked to this file in the settings.py file. By typing 'git add .', 'git commit -m "commit-message"', and 'git push', all of my static and media files are uploaded to my s3 bucket.
20. To add media image files to s3, I clicked on the Create Folder button in my project overview on the dashboard of my AWS s3 account. I called it 'media' and inside it I clicked on the Upload and Add Files buttons and uploaded all of the images for my project. Having done that I clicked on the Next button and in the Manage Public Permissions section I chose Grant Public Read Access To This Object(s). I then clicked the Upload button.
21. I linked Stripe to my s3 account by getting the test Publishable Key from my Stripe dashboard and inserting it into the config variables section of my heroku dashboard. 
22. Then I created a new endpoint for my stripe webhooks by going to the webhooks section of the Stripe dashboard. I added my deployed heroku project's url as the endpoint. I got the Signing Secret key that was revealed after setting up the endpoint and inserted it into the config variables section of my heroku project.




# Credits
## Photos:
### Carousel images on index.html
1. Guitar store image taken from https://www.westwoodmusic.com (https://www.westwoodmusic.com/wp-content/uploads/2014/12/sales-floor.jpg) 
2. Other guitar store image taken from https://www.montreal360virtualtour.com/ (https://www.montreal360virtualtour.com/wp-content/uploads/2017/12/Steve_s-Music-Store-15.jpg)
3. Drum store taken from https://www.expressmusic.co.uk (https://www.expressmusic.co.uk/images/store/cov%208_rs.jpg)

### Category Images on index.html
1. Drum set taken from https://www.explorersdrums.com (https://www.explorersdrums.com/assets/images/ACCENTRED.jpg).
2. Guitar taken from https://www.richtonemusic.co.uk (http://images.richtonemusic.co.uk/product/MARTINHD-28-REIMAGINEDb.jpg).
3. Bass guitar taken from https://www.gear4music.com (https://d1aeri3ty3izns.cloudfront.net/media/26/262795/1200/preview.jpg).
4. Trumpet taken from https://www.discoversinging.co.uk (https://i2.wp.com/www.discoversinging.co.uk/wp-content/uploads/2013/08/trumpet.jpg).
5. Viola taken from https://www.victoriabuzz.com (https://www.victoriabuzz.com/wp-content/uploads/2017/12/56386c126c656484fa101f680f7e111e.jpg).
6. Microphone taken from https://www.musicstorelive.com (https://media.musicstorelive.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/a/samsn-r21s_1.jpg)

### Empty Shopping cart on empty cart.html page
1. Shopping cart taken from https://www.dreamstime.com/ (https://thumbs.dreamstime.com/b/empty-shopping-cart-side-view-isolated-white-background-31773785.jpg)

### Forms
1. Piano shop image on login.html taken from https://www.sweetwater.com/ (https://media.sweetwater.com/about/press-releases/images/Piano_Store.jpg).
2. Guitar display image on registraion page taken from https://content.guitarvillage.co.uk/ (https://content.guitarvillage.co.uk/images/2016/02/PRSRoomWideOptimised.jpg)

## 
Both my mentor Akshat Garg and many people on Slack were very helpful in dealing with bugs encountered during development.