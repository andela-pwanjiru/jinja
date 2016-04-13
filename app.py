from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('child.html', my_string="Best fruits", my_list=["mangos","pineapples","strawberries","pears","oranges"])


@app.route("/home")
def home():
    return render_template('child.html', my_string="Amazing games!", my_list=["skydiving","swimming","hockey","cycling","running"], title="home")


@app.route("/about")
def about():
    return render_template('child.html', my_string="Everything cool!", my_list=[0,1,2,3,4,5], title="About")


@app.route("/contact")
def contact():
    return render_template('child.html', my_string="TIA!", my_list=[0,1,2,3,4,5], title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
