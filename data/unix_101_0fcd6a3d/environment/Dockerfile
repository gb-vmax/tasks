FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN date +%s > /home/user/start_time.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

