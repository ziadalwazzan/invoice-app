## Preview



https://github.com/ziadalwazzan/invoice-app/assets/51064118/4af90601-cc32-4622-99cd-6d58544a0a9e



## Available Scripts:

In the client directory, you can run:

  cmd:  `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

  cmd:  `npm run start-backend`

Runs the flask app.\
Server will listen on [http://localhost:5000].

## App Set Up:

Note:
---

- npm and python must be installed in order for this app to run.
- After setting up Project, create a `server/invoices/` and `server/qoutes/` directory

Client setup:
---

1. Install Node.js 20.5 / NPM 9.8

2. Run: `npm install` in client directory

3. install PM2 package which will be used to run the app.\
  PM2 is a deamon proccess manager that is used to manage the client/server processes in the background.\
  cmd: `npm install pm2 -g`

venv setup:
---

1. Install Python 3.11

Mac: `brew install python`
Windows: Use python installer
(https://www.python.org/downloads/)

2. Navigate to the invoice-app/ directory and run:\
  `[YOUR_PYTHON_INSTANCE] -m venv venv`

3. Activate the instance:\
  cmd: `source venv/bin/activate`

4. Install the server dependencies using the following command:\
cmd: `python3 -m pip install -r requirements.txt`\
(The install command must be ran with the venv activated in order to use the correct python/pip instances)

Server setup:
---

1. Navigate to the invoice-app/server/ Directory
2. With the venv activated (Or using the correct Python instance/dependencies) initialize the SQLITE DB:\
cmd: `[VENV_PYTHON_INSTANCE] init_db.py`


## Starting the App:

1. Navigate to the invoice-app/client/ directory.
2. Start the Flask server: \
    cmd: `pm2 start npm --name invoice-server -- run start-backend --`
3. Start the React client: \
    cmd: `pm2 start npm --name "invoice-client" -- start`

Note:
---
To check PM2 running proccesses run:\
cmd: `pm2 list`



















