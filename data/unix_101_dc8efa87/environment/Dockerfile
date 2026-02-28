FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/temp
RUN echo 'lock' > /home/user/temp/session.lock
RUN chown -R user:user /home/user
RUN su - user -c "bash -c 'tail -f /home/user/temp/session.lock > /dev/null &'"
RUN sleep 1
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

