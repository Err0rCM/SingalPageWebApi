FROM python:3.8.12

COPY ./app /app
WORKDIR /app

ENV PYTHONUNBUFFERED=0

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN rm requirements.txt


RUN useradd -m ctf \
    && chown ctf:ctf /app

USER ctf

EXPOSE 5000
CMD python3 app.py
# CMD gunicorn -c gunicorn.conf.py --debug app:app
# CMD gunicorn -c gunicorn.conf.py app:app
# CMD ["gunicorn", "-c", "./gunicorn.conf.py", "--debug", "app:app"]
# CMD python3 test.py
#CMD python3 app.py
# CMD gunicorn -b 0.0.0.0:5000 -w 6 --threads 6  --log-level 'debug' app:app
