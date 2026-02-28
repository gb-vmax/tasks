FROM unix101-base:latest

USER root
RUN printf "alpha\nbeta\ngamma\n" > /home/user/info.log
RUN gzip /home/user/info.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

