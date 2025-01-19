from flask import Flask, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)
app.debug = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG'] = True



debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)

@app.route("/")
def show_home():
    """Shows all pets by name"""
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} was added!")
        
        return redirect("/")
    else:
        return render_template('add_pet.html', form=form)