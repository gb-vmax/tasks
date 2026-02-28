FROM unix101-base:latest

USER root
RUN su user -c 'bash -c "sleep 60" &'
RUN su user -c 'bash -c "sleep 60" &'
RUN sleep 1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

