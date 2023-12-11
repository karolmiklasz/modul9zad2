from flask import Flask, render_template, redirect, url_for
from forms import LibraryForm
from models import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", items=library.all())

@app.route("/add_item/", methods=["GET", "POST"])
def add_item():
    form = LibraryForm()
    if form.validate_on_submit():
        library.create(form.data)
        library.save_all()
        return redirect(url_for("home"))
    return render_template("add_item.html", form=form)

@app.route("/edit_item/<int:item_id>/", methods=["GET", "POST"])
def edit_item(item_id):
    item = library.get(item_id - 1)
    form = LibraryForm(obj=item)
    if form.validate_on_submit():
        library.update(item_id - 1, form.data)
        return redirect(url_for("home"))
    return render_template("edit_item.html", form=form, item_id=item_id)

if __name__ == "__main__":
    app.run(debug=True)
