# Makefile for project setup and commands

install:
	pip install -r requirements.txt

run-admin:
	streamlit run admin.py

run-dashboard:
	streamlit run dashboard.py

test:
	python test_db_connection.py

docker-build:
	docker build -t multitenant-app .

docker-run:
	docker run -p 8501:8501 --env-file .env multitenant-app
