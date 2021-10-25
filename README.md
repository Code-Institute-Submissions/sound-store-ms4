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
I designed the site to be as simplistic as possible to use. I didn't want it to be too visually cluttered.
## Colours Used
1. Dark navy - #011627
2. Light green - #2EC4B6
3. Red - #e71d36
4. Yellow - #ff9f1c
5. Dark blue - #122c34
6. Light Blue - #36597D
7. Lighter Blue - #36597D
8. White - #fdfffc
9. Orange - #ff9f1c
10. Green - #2ec4bc
11. White
12. Gold


## Fonts Used
1. Sonsie One - This font reminds me of some of the Fender guitars or Gibson guitars logos and therefore I thought it would be a good fit for the site.
2. Roboto - Easy to read font used in the navbar links
3. Tenor Sans - A nice font to render the product names font in.


# Bugs Encountered
### Webhooks bugs
1. When attempting to send webhook test events, I was receiving a result of "Test webhook error:401". This was fixed by opening up the ports tab in Gitpod and making the 8000 port public.
2. On another occasion while trying to send a test webhook, I was receiving a result of "Test webhook error:404". This was fixed by updating the region code, i.e. "...eu(number)..." in the gitpod workspace url. This number appeared to change somewhat regularly and so needed to be updated in the stripe endpoint url in the stripe dashboard. 
3. Due to the superuser being created at the beginning of development before the profiles app was created, the profiles app did not recognise the superuser name and threw an error 404 screen in response to my attempting to login to admin. This was fixed by commenting out the 'if created:' statement in the profiles.models file... {show picture} ... , logging in with the superuser name and password, and then uncommenting the code. On both the commenting and uncommenting of the 'if' statement, the line inside was indented appropriately in order for the code to work.

### Product Admin Bugs
1. When Testing the add product form in add_product.html I successfully added numerous products to the database. I then deleted these products in the database. The result of this was that my site seemed to become totally unusable. When loading my site using 'python3 manage.py runserver' I was getting a 404 error saying that my home page was not found. I tried undoing all the work I had done leading to this error and redoing it but it did not work. Finally I found a post on Slack related to this and realised that the products deleted from my database were in my shopping cart and thus were cached in the entire project. As per the advice in that post I deleted the sessionid from developer tools and this fixed the error. 



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