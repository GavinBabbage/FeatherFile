pipenv:
	pip install pipenv
	pipenv shell

run:
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver


clean:
	rm -rf venv
	rm -rf input
	find -iname "*.pyc" -delete
      
