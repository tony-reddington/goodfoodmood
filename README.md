[View GoodFoodMood website here](https://good-food-mood.herokuapp.com/)

# GoodFoodMood
![responsive website](static/images/responsive-image.JPG)

## The goal of this website is to share cooking recipes that will be populated by both the owner and registered users that appear on tiles on the main page. Each user has their own profile page where they can store, edit or delete their uploaded recipes.

### User Experience (UX)

#### The user goals will be to:
* Easily navigate through the website
* Ability to access the website using multiple devices
* Create an account to store created recipes
* Create recipes
* Replace recipes
* Update recipes
* Delete created recipes
* Search for recipes

### User Stories

#### As a user, I want - 
* the navigation bar clearly visible so I can easily navigate the website.
* a page displaying all uploaded recipes.
* the website responsive across devices so I can swap and change devices as I wish.
* the page laid out neatly so that I can find information effortlessly.
* to create a profile that will be home to all my recipes and allow me to create then replace, update and delete recipes that i have uploaded to the website.

### Site owner goals

#### As the site owner, I want - 
* to provide a simple navigation display making it easy for users to navigate through the website.
* to display all recipes on the home page.
* to provide responsiveness across all device screen sizes.
* to lay out all recipe information as clearly as possibly so users can find everything with ease.
* to allow users to create profiles, giving them access to create, replace, update and delete recipes.

### Design

#### Colour Scheme
 - I researched multiple recipe websites to check their colour schemes and ended up with the colours below. The colours used across the website are Purple which is said to invoke creativity, Yellow that invokes happiness with Grey for borders/shading and classic Black and White being used for font colour.

    ![](static/images/colour-scheme.JPG)

#### Typography
 - The font used across the website is Monserrat because of it's simplicity and legibility with Sans Serif as the fall back font.

#### Imagery
 - The only image used for the website is on the index.html page. It contains food items around the parimeter of the image and fits in with the recipe website theme. The rest of the recipe images are uploaded by the user/admin via a link and these are retrieved from Mongodb database.

#### Wireframes

* [Home wireframe](#)

* [Login wireframe](#)

* [Register wireframe](#)

* [Profile wireframe](#)

* [Add Recipe wireframe](#)

### Existing Features
 * The website is made up of 5 x pages. 2 of which are only visible to a user when they create a profile.
 * #### Home page
   * The Home page is made up of a brand logo and navigation bar along the top of the page. The navbar scrolls with the user to help them keep on track. The navigation bar changes to a hamburger button on smaller screens.
   * A background image appears below the navbar with a welcome message overlay in the centre.
   * Recipes are retrieved from MongoDB and displayed in a card view showing the user an overview of the recipe name, image and description. A button can then be clicked to view the full recipe.
   * Social media icons for Twitter, Facebook and Instagram appear in the footer.
 * #### Login page
   * A form is displayed over the main background image with inputs for a user to enter their username and password.
   * A button then checks that the username and password exists within the MongoDB database and returns a flash message.
   * Once successful the user will have access to their profile page and an the Add Recipe button.
 * #### Register page
   * A form is displayed over the main background image with inputs for a user to enter their username,password and a field to verify their entered password.
   * A button then adds the username and password to the MongoDB database if successful and returns a flash message above the form.
   * The user will then have access to their profile page and an the Add Recipe button.
 * #### Profile page
   * A welcome "username" message appears over the main background image.
   * The users uploaded recipes are retrieved from MongoDB and displayed in cards.
   * The cards house 2 x buttons for editing and deleting the users recipes and both activate modal pop ups.
   * The editing modal display's a form showing all the data the user previously input allowing them to make edits or additions where requiredwith a button along the bottom to submit the changes to MongoDB.
   * The delete modal displays a warning to users to confirm that their intention is to delete with a button on the bottom which deletes the recipe from MongoDB.
 * #### Add Recipe page
   * The add recipe page contains an user instruction and button to activate a form modal.
   * The add recipe form modal displays provides a user with labels and fields to enter their recipe. The add recipe button at eh end of the form submits the recipe to MongoDB that will in tirn be displayed on the homepage and on their profile.

### Features for future implimentation
 * Different sections for meal types
 * Search function
 * Remove imported css to improve page loading speed.
 * A more dynamic relational database to avoid so many if statements for inputs. 
## Technology Used

### Languages used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### Frameworks/Libraries and Programs used
1.  [Balsamiq](https://balsamiq.com/)
    - Balsamic was used to build wireframes for the website pages.
2.  [Font Awesome](https://fontawesome.com/)
    - Font awesome was used for the social media icons in the footer and the icons on the login/registration forms.
3.  [Google fonts](https://fonts.google.com/)
    - The Monserrat font that i used across the website was taken from Google fonts.
4.  [Istockphoto](https://www.istockphoto.com/)
    - Istockphoto was used for all the main background website image.
5.  [TinyJPG](https://tinyjpg.com/)
    - Tinyjpg was used to reduce the size of all the background image.
6.  [Befunky photo editor](https://www.befunky.com/)
    - Befunky photo editor was used to resize images.
7.  [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used for the recipe cards and to make the website more responsive in certain areas.
8.  [Coolers](https://coolors.co/)
    - Coolers was used to help generate a colour palette for the entire site.
9.  [MongoDB](https://www.mongodb.com/)
    - MongoDB holds the Recipes database that holds the recipe data and user credentials.
10. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask framework was used to build the website. 
11. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security)
    - Werkzeug was user to generate hashed passwords.
12. [Favicon](https://favicon.io/)
    - Favicon.io was used to create the website favicon.
13. [MDB Bootstrap](https://mdbootstrap.com/docs/standard/)
    - MDB bootstrap was used to create the modals.
14. [Start Bootstrap](https://startbootstrap.com/)
    - Start Bootstrap was used to create the structure of the website using the Clean Blog theme.
15. [Web Formatter](https://webformatter.com/)
    - Web Formatter was used to format the CSS stylesheet and all HTML pages to make the code easier to read.
16. [Gitpod](https://gitpod.io/)
    - Gitpod was used to write the website code.
17. [GitHub](https://github.com/)
    - GitHub was used to host the code and website contents.

