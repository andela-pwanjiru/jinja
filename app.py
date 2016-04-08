from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('macro.py', my_string="This is awesome", my_list=["mangos","pineapples","strawberries","pears","oranges"])

@app.route("/home")
def home():
    return render_template('macro.py', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="home")

@app.route("/about")
def about():
    return render_template('macro.py', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="About")


@app.route("/contact")
def contact():
    return render_template('macro.py', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
