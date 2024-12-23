FROM python:3.13-alpine

RUN addgroup -S pygrp && adduser -S pyusr -G pygrp

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apk add uv

WORKDIR /app
RUN chown pyusr:pygrp /app

COPY --chown=pyusr:pygrp . .

USER pyusr

RUN uv sync || echo "Environment prepared during build"

CMD ["uv", "run", "fastapi", "run", "src/app.py"]
