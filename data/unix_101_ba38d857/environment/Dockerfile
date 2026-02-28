FROM unix101-base:latest

USER root
RUN pkill -u user sleep || true
RUN su user -c 'sleep 180 &'
RUN su user -c 'sleep 180 &'
RUN su user -c 'sleep 180 &'
RUN sleep 1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

