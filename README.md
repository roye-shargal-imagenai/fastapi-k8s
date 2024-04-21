start virtual env:
source venv/bin/activate

run app:
uvicorn main:app --reload

run docker image: 
docker run -d -p 8000:8000 fast-api 
