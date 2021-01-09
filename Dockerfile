FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn core:app --host 0.0.0.0 --port 8000 --reload