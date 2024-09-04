from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"

class SearchForm(FlaskForm):
    search_query = StringField("Search")
    submit = SubmitField("Submit")

@app.route("/")
def index():
    return render_template("index.html", title="Home Page")

@app.route("/search", methods=["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # Do something with the search query
        pass
    return render_template("search_results.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)