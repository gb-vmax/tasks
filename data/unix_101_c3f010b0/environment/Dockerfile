FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN su user -c 'sleep 1000 &'
RUN su user -c 'sleep 1000 &'
RUN sleep 0.2
RUN ps -u user -o pid= | grep -E '^[0-9]+$' > /home/user/userpids.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

