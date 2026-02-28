FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN runuser -l user -c 'sleep 300 &'
RUN runuser -l user -c 'sleep 500 &'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

