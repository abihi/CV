# API setup
Create virtualenv:
1.  $ cd CV/api
2.  $ python3 -m venv venv (linux) / py -m venv venv (windows)
3.  $ source venv/bin/activate (linux) / .\venv\Scripts\activate (windows)
4.  $ pip install -r requirements.txt


# Run app & update requirements.txt
*   $ uvicorn main:app --reload
*   $ deactivate deactivates the Virtualenvironment
*   $ pip freeze > requirements.txt