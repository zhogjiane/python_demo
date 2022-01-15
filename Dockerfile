FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app
WORKDIR /app
# 设定对外端口
EXPOSE 80
CMD ["python3", "main.py"]