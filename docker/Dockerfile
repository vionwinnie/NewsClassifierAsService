FROM python:3.7

WORKDIR /app

RUN pip install pandas numpy scikit-learn flask gunicorn

ADD main.py main.py
ADD ./model ./model

EXPOSE 5000

CMD [ "ls", "-la"]
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "main:app" ]
