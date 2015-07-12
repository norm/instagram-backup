import os

from flask import (
    Flask,
    render_template,
    request,
)

from instagram.client import InstagramAPI

DEBUG = True
ID = os.getenv('INSTAGRAM_CLIENT_ID')
SECRET = os.getenv('INSTAGRAM_SECRET')
URI = 'http://localhost:4726/'

instagram = InstagramAPI(
    client_id=ID,
    client_secret=SECRET,
    redirect_uri=URI
)
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def homepage():
    code = request.args.get('code', None)

    if code is None:
        return render_template('homepage.html')
    else:
        token, user_data = \
            instagram.exchange_code_for_access_token(code)
        user_id = user_data['id']
        return render_template('code.html', token=token, user_id=user_id)


if __name__ == "__main__":
    app.run(port=4726, debug=True)
