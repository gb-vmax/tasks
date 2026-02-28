FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN sleep 1000 & echo $! > /home/user/sleeppid.txt
RUN sleep 0.2
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

