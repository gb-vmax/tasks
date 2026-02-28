FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/env
RUN echo 'alpha beta gamma' > /home/user/env/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

