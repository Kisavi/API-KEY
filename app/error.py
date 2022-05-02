from flask import render_template
from app import app


@app.errorhandler(404)
def err(error):
    """
    function to render 404 error page
    """
    return render_template('err.html'), 404
