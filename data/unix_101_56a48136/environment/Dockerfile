FROM unix101-base:latest

USER root
RUN printf "Hello SHA256!\n" > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

