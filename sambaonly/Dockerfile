FROM ubuntu:18.04

# install what we need: Samba

RUN apt-get update && apt-get install -y samba

# see https://github.com/dperson/samba
# https://github.com/crops/samba

# copy /workdir and /app to the the container

COPY workdir /workdir
COPY app /app

RUN chown -R nobody:nogroup /workdir

EXPOSE 445

CMD ["/usr/sbin/smbd", "-FS", "-s", "/app/smb.conf"]
