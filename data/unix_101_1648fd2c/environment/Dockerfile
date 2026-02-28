FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN runuser -l user -c 'bash -c "sleep 100" &'
RUN runuser -l user -c 'bash -c "sleep 200" &'
RUN runuser -l user -c 'bash -c "sleep 300" &'
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

