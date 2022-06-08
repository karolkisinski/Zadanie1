FROM scratch
LABEL MAINTAINER="Karol Kisiński"
ADD images/alpine-minirootfs-3.16.0-x86_64.tar.gz /
WORKDIR /app
ADD /app /app

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.16/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add py-pip && \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt

CMD ["python3", "app.py"]
