import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    """
    Takes user to the index.html page.
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows user to create and account, checks the if/elif statements
    and then check's if the user has previously been registered.
    On successful registration, the user is redirected to index.html
    """
    if request.method == "POST":
        user = mongo.db.users
        username = request.form.get("username")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm_password")
        active_user = user.find_one({"username": username.lower()})

        if active_user:
            flash("The selected username already exists", category="error")
            return redirect(url_for("register"))
        elif len(username) < 5:
            flash("Username must be more than 5 x characters long",
                  category="error")
            return redirect(url_for("register"))
        elif len(password) < 5:
            flash("Password must be more than 7 x characters long",
                  category="error")
            return redirect(url_for("register"))
        elif password != confirmed_password:
            flash("The passwords entered do not match", category="error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password, method="sha256")
        }
        user.insert_one(register)

        session["username"] = request.form.get("username").lower()
        flash("You have been successfully registered", category="success")
        return redirect(url_for("profile", username=session["username"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows user to log into their account. The function checks if the entered
    username exists and if it does, then checks the stored db password
    against the password the user entered on the form. If successful the
    user is then redirected to their profile. If the username or password
    doesn't match the stored data, the user recieves a flash notification
    and is redirected to the login page.
    """
    if request.method == "POST":
        user = mongo.db.users
        current_user = user.find_one(
            {"username": request.form.get("username").lower()})
        if current_user:
            if check_password_hash(
                    current_user["password"],
                    request.form.get("password")):
                session["username"] = request.form.get("username").lower()
                return redirect(url_for("profile",
                                username=session["username"]))
            else:
                flash("The wrong username/password has been entered")
                return redirect(url_for("login"))
        else:
            flash("The wrong username/password has been entered")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Allows a user to access their profile page. The profile page accesses
    the recipes and username variable to display both on the profile page.
    """
    user = mongo.db.users
    recipes = list(mongo.db.recipes.find())
    username = user.find_one({"username": session["username"]})["username"]
    """
    Check if cookies has recorded session and directs the user to their profile
    page otherwise directs them to the login page.
    """
    if session["username"]:
        return render_template("profile.html", recipes=recipes,
                               username=username)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Allows user to logout. The session username is
    removed and the user is redirected back to index.html"
    """
    session.pop("username")
    flash("You have been successfully logged out")
    return redirect(url_for("index"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Allows user to add recipes. The recipe variable gets all inputed data from
    the addrecipe-form and adds to the mongo db recipes database. The user is
    then redirected back to the home page with a flashed messages and their
    recipe is displayed.
    """
    if request.method == "POST":
        get_recipe = request.form.get
        recipe = {
           "recipe_name": get_recipe("recipe_name"),
           "image_url": get_recipe("image_url"),
           "description": get_recipe("description"),
           "dietary_info": get_recipe("dietary_info"),
           "ingredients_1": get_recipe("ingredients_1"),
           "ingredients_2": get_recipe("ingredients_2"),
           "ingredients_3": get_recipe("ingredients_3"),
           "ingredients_4": get_recipe("ingredients_4"),
           "ingredients_5": get_recipe("ingredients_5"),
           "ingredients_6": get_recipe("ingredients_6"),
           "ingredients_7": get_recipe("ingredients_7"),
           "ingredients_8": get_recipe("ingredients_8"),
           "directions_1": get_recipe("directions_1"),
           "directions_2": get_recipe("directions_2"),
           "directions_3": get_recipe("directions_3"),
           "directions_4": get_recipe("directions_4"),
           "directions_5": get_recipe("directions_5"),
           "directions_6": get_recipe("directions_6"),
           "directions_7": get_recipe("directions_7"),
           "directions_8": get_recipe("directions_8"),
           "prep_time": get_recipe("prep_time"),
           "cook_time": get_recipe("cook_time"),
           "total_time": get_recipe("total_time"),
           "servings": get_recipe("servings"),
           "cooking_temperature": get_recipe("cooking_temperature"),
           "recipe_by": session["username"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added successfully")
        return redirect(url_for("index"))
    return render_template("addrecipe.html")


@app.route("/update<recipe_id>", methods=["GET", "POST"])
def update_recipe(recipe_id):
    """
    Allows user to update recipes. The new update variable holds the updated
    data and updated the database based on the recipes id accessed. Flashes
    a message that the recipe has been updated and redirects the user back
    to the home page.
    """
    if request.method == "POST":
        get_recipe = request.form.get
        new_update = {
           "recipe_name": get_recipe("recipe_name"),
           "image_url": get_recipe("image_url"),
           "description": get_recipe("description"),
           "dietary_info": get_recipe("dietary_info"),
           "ingredients_1": get_recipe("ingredients_1"),
           "ingredients_2": get_recipe("ingredients_2"),
           "ingredients_3": get_recipe("ingredients_3"),
           "ingredients_4": get_recipe("ingredients_4"),
           "ingredients_5": get_recipe("ingredients_5"),
           "ingredients_6": get_recipe("ingredients_6"),
           "ingredients_7": get_recipe("ingredients_7"),
           "ingredients_8": get_recipe("ingredients_8"),
           "directions_1": get_recipe("directions_1"),
           "directions_2": get_recipe("directions_2"),
           "directions_3": get_recipe("directions_3"),
           "directions_4": get_recipe("directions_4"),
           "directions_5": get_recipe("directions_5"),
           "directions_6": get_recipe("directions_6"),
           "directions_7": get_recipe("directions_7"),
           "directions_8": get_recipe("directions_8"),
           "prep_time": get_recipe("prep_time"),
           "cook_time": get_recipe("cook_time"),
           "total_time": get_recipe("total_time"),
           "servings": get_recipe("servings"),
           "cooking_temperature": get_recipe("cooking_temperature"),
           "recipe_by": session["username"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, new_update)
        flash("Your recipe has been updated successfully")
        return redirect(url_for("index"))
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("profile.html", recipes=recipes)


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    """
    Allows user to delete recipes. The selected recipe is captured by it's id
    and the deleted. The user is then returned to the homepage and flashed a
    message to let them know the recipe has been successfully deleted"
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("The selected Recipe has been successfully deleted")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_available(e):
    """
    If a 404 error occurs, the user is directed to a custom 404 page.
    """
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):
    """
    If a 500 error occurs, the user is directed to a custom 500 page.
    """
    return render_template('500.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
