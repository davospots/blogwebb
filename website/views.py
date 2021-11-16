from flask import Blueprint, render_template
from .requests import get_quotes

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():


    quote = get_quotes()

    return render_template("home.html",quote = quote)
