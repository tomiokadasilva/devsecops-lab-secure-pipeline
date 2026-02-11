FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /home/appuser/app

COPY --chown=appuser:appuser . .

USER appuser
RUN pip install --user --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]