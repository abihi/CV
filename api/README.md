# API setup
Create virtualenv:
1.  $ cd api
2.  $ py -m venv venv 
3.  $ .\venv\Scripts\activate 
4.  $ pip install -r requirements.txt


# Run app & update requirements.txt
*   $ uvicorn app.main:app --reload
*   $ deactivate (deactivates the Virtualenvironment)
*   $ pip freeze > requirements.txt
