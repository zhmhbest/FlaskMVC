from app import the_app as app


@app.route("/")
def the_root():
    # from flask import redirect
    # return redirect(app.config['HOME_PAGE'])
    return "Hello"
