FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    openssh-server \
    sudo \
    vim \
    && mkdir /var/run/sshd

RUN useradd -m -s /bin/bash ansible && \
    echo "ansible:ansible" | chpasswd && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
