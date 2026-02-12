FROM python:3.13-slim

WORKDIR APP/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 5000

CMD ["gunivorn", "--bind", "0.0.0.0:5000", "wsgi:app"]