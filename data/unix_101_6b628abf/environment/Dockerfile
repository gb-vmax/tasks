FROM unix101-base:latest

USER root
RUN echo 'export TEMP_VAR=hello_world' >> /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

