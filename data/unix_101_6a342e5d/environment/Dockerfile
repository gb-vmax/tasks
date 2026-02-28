FROM unix101-base:latest

USER root
RUN mkdir -p /logs/verifier
RUN hostnamectl set-hostname agent-training-host
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

