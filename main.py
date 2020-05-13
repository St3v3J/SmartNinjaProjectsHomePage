import datetime
from flask import Flask, render_template, request, make_response


app = Flask(__name__)


@app.route("/")
def index():
    some_text = "This message is from Steve...HEY!."
    current_year = datetime.datetime.now().year

    cities = ["Anaheim", "Los Angeles", "Miami", "Santa Clara", "Las Vegas"]

    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/about-me", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    response = make_response(render_template("success.html"))
    response.set_cookie("user_name", contact_name)

    return response


if __name__ == '__main__':
    app.run()