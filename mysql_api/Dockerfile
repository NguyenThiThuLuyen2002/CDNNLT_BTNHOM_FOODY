FROM python:3.9.16-slim-buster
COPY ./ /api
RUN pip install fastapi uvicorn mysql-connector-python csv os
WORKDIR ./api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9002"]
EXPOSE 9002