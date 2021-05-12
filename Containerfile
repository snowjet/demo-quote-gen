FROM registry.access.redhat.com/ubi8/python-38

ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

USER 0
COPY quotegen /usr/src/app/quotegen
COPY pypi /tmp/pypi
RUN chown -R 1001:0 /usr/src/app/quotegen && chown -R 1001:0 /tmp/pypi
USER 1001

WORKDIR /usr/src/app/quotegen
RUN pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py"]