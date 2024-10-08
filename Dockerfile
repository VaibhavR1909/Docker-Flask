FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "demo.py" ] 
