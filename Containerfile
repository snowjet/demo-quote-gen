FROM registry.access.redhat.com/ubi8/python-38

ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

COPY quotegen /usr/src/app/quotegen

WORKDIR /usr/src/app/quotegen
RUN pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py"]