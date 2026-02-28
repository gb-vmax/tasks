FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN truncate -s 0 /home/user/input.txt
RUN rm -f /home/user/empty.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

