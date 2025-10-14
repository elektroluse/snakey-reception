FROM python:3.13.7-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN apt-get install -y make

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY src/requirements.txt .
 
# no virtual env
RUN uv pip install -r requirements.txt --system 

COPY src/ .

EXPOSE 8000

CMD ["./entrypoint.sh"]