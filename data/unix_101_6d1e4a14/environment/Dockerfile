FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testdir
RUN rm -f /home/user/max_name_len.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

