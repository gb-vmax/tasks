FROM unix101-base:latest

USER root
RUN mkdir -p /logs/verifier
RUN mkdir -p /home/user
RUN touch /home/user/interfaces.json
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

