FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN printf "Event started\nEvent processing\n" > /home/user/logs/event.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

