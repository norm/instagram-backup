import os
import sys
import requests

from flask import (
    Flask,
    render_template,
    request,
)


ID = os.getenv('INSTAGRAM_CLIENT_ID', None)
SECRET = os.getenv('INSTAGRAM_SECRET', None)

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def homepage():
    code = request.args.get('code', None)

    if code is None:
        return render_template('homepage.html', client_id=ID)
    else:
        api_response = requests.post(
            'https://api.instagram.com/oauth/access_token',
            data={
                'client_id': ID,
                'client_secret': SECRET,
                'code': code,
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:4726/',
            }
        )

        json_data = api_response.json()

        return render_template(
            'code.html',
            token=json_data['access_token'],
            user_id=json_data['user']['id'],
        )


if __name__ == "__main__":
    if ID is None or SECRET is None:
        sys.exit('Requires INSTAGRAM_CLIENT_ID and INSTAGRAM_SECRET '
                 'environment variables.')

    app.run(port=4726, debug=True)
