FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'error: failed to load\nwarning: deprecated api\ninfo: process started' > /home/user/data/info.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

