instagram-backup
================

Download a local copy of all of your instagram photos including their metadata
(such as description, likes, comments, etc).

## Instructions

0.  *Setup python requirements.*

    This is written in python, and requires a couple of libraries to be
    installed before it will work.

    If you are familiar with python programming, set up a virtualenv and
    install the requirements.

    If you don't know python, this command should be enough on OS X and Linux
    computers:

    ```
    sudo pip install -r requirements.txt
    ```

1.  *Create an application.*

    You need to create a new client application within Instagram using your
    account. Go to [Manage Clients][mc] within the developer dashboard and
    click *Register a New Client*.

    Enter anything you like for the name, description and website URL.
    The *Redirect URL* should be `http://localhost:4726/`.

    ![Creating your application](https://raw.github.com/norm/instagram-backup/master/create.png)

    Once created, the information of your application will contain two
    strings, labelled *Client ID* and *Client Secret*, like so (this image is
    just for illustration, the keys shown won't work):

    ![Your client keys](https://raw.github.com/norm/instagram-backup/master/keys.png)

    Copy and paste them into your terminal, like so:

    ```
    export INSTAGRAM_CLIENT_ID=<your client id>
    export INSTAGRAM_SECRET=<your client secret>
    ```

[mc]:https://instagram.com/developer/clients/manage/


2.  *Get a client authentication token.*

    You then need to get an authentication token, which allows the backup
    script to behave *as you* on Instagram. Run the following command in
    your terminal

    ```
    python get_token.py
    ```

    then open your browser to <http://localhost:4726/>. Click the link
    to get your token — this will take you to Instagram to authorise,
    then present you with two more values to export to your Terminal.

    Stop the previous command in your Terminal by pressing Control and C at
    the same time. Then copy and paste the values from the browser.


3.  *Backup your photos.*

    Run the following script in your Terminal:

    ```
    python backup.py
    ```

    This will create a directory called `backup` and fetch all of your
    Instagram photos.
