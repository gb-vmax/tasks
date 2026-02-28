FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN nohup sleep 180 >/home/user/sleeplog2.txt 2>&1 & echo $! >/home/user/pid2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

