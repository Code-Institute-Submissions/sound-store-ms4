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
3. Jquery - A simpler form of javascript
4. Bootstrap - A css framework  
5. Favicon (https://favicon.io/favicon-generator/) - To get icon for the sites tab.
6. Font Awesome (https://fontawesome.com/v4.7/icons/) - To get icons for social media / shopping cart etc.
7. Google Fonts - (https://fonts.google.com/) - To get letter styling fonts for the site.
8. Balsamiq - Used to make wireframes.
9. Stripe - Used to process payments in the store
10. PostgreSQL - Database used on the deployed site.
11. SQlite3 - Database used during development.
12. Github - Used to store my project.
13. Coolors (https://coolors.co/) - To generate a colour pallette to choose from.


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
3. Tenor Sans - A readable font to render the product names font in.

## Images
The site relies heavily on images. The home page uses a carousel of three images, the login page and registration also use an image on each. These five images are used to represent the actual walk-in store. On the index page are clickable instrument-image links to the product categories. Also there are a large number of product images on the site.


# Bugs Encountered
### Webhooks bugs
1. When attempting to send webhook test events, I was receiving a result of "Test webhook error:401". This was fixed by opening up the ports tab in Gitpod and making the 8000 port public.
2. On another occasion while trying to send a test webhook, I was receiving a result of "Test webhook error:404". This was fixed by updating the region code, i.e. "...eu(number)..." in the gitpod workspace url. This number appeared to change somewhat regularly and so needed to be updated in the stripe endpoint url in the stripe dashboard. 
3. Due to the superuser being created at the beginning of development before the profiles app was created, the profiles app did not recognise the superuser name and threw an error 404 screen in response to my attempting to login to admin. This was fixed by commenting out the 'if created:' statement in the profiles.models file... {show picture} ... , logging in with the superuser name and password, and then uncommenting the code. On both the commenting and uncommenting of the 'if' statement, the line inside was indented appropriately in order for the code to work.

### Product Admin Bugs
1. When Testing the admin-only add product form in add_product.html, I successfully added numerous products to the store. I then deleted these products in the admin database. The result of this was that my site become totally unusable. When loading my site using 'python3 manage.py runserver' I was getting a 404 error saying that my home page was not found. I tried undoing all the work I had done leading to this error and redoing it but it did not fix the issue. Finally I found a post on Slack related to this and realised that the products deleted from my database were in my shopping cart at the time and thus were cached in the entire project. I deleted the sessionid from developer tools and this fixed the error. 



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