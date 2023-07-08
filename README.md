## Available Scripts

In the project directory, you can run:

  cmd:  `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

  cmd:  `npm run start-backend`

Runs the flask app.\
Server will listen on [http://localhost:5000].

 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////  App Set Up ////////////////////////////////////////////////////////////////////////// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Note:
------
- npm and python must be installed in order for this app to run.

------------------
|| Client setup ||
------------------

1. Install npm

2. Run: 'npm install' in client directory

3. install PM2 package and run the client using PM2 deamon proccess manager
  cmd: 'npm install pm2 -g' 

------------------
||  venv setup  ||
------------------

1. Install Python 3.11

Mac: 'brew install python'
Windows: Use python installer
(https://www.python.org/downloads/)

2. Navigate to the invoice-app/ directory and run:
  cmd: 'source venv/bin/activate'

This will set up the python virtual environment so that the app has the required dependencies in the venv directory.

------------------
|| Server setup ||
------------------

1. While in invoice-app/client Run: 
  cmd: 'pm2 start npm -- run start-backend --'
























