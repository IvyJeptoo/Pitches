from . import main

@main.route('/')
def home():
    return "<h1> test</h1>"

