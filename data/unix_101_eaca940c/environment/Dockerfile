FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN touch /home/user/conflict.lock
RUN rm -f /home/user/test.txt
RUN chown -R user:user /home/user
RUN su user -c 'flock -x /home/user/conflict.lock sleep 10 &'
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

