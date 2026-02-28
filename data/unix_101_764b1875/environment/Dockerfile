FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo -e "Started application\nUser logged in\nError: failed to open socket" > /home/user/logs/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

