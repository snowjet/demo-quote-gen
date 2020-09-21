FROM registry.access.redhat.com/ubi8/python-38

ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

COPY quotegen /usr/src/app/quotegen
COPY pypi /tmp/pypi

WORKDIR /usr/src/app/quotegen
RUN pip install -U pip && \
    pip install --no-index --find-links=/tmp/pypi --no-cache-dir -r requirements.txt && \
    rm -rf /tmp/pypi

CMD [ "python", "app.py"]