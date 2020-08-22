# API setup
Create virtualenv:
1.  $ cd api
2.  $ py -m venv venv 
3.  $ .\venv\Scripts\activate 
4.  $ pip install -r requirements.txt


# Run app & update requirements.txt
*   $ uvicorn app:app --reload
*   $ deactivate (deactivates the Virtualenvironment)
*   $ pip freeze > requirements.txt

# Run tests & linter
*   $ python -m pytest
*   $ flake8 --statistics
