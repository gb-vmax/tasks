FROM unix101-base:latest

USER root
RUN echo 'export MYVAR=hello' > /home/user/envvars.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

