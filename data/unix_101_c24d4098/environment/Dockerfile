FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/alpha
RUN mkdir -p /home/user/data/beta
RUN echo -n 'unix' > /home/user/data/file1.txt
RUN head -c 10 /dev/zero > /home/user/data/alpha/a.bin
RUN echo 'hello' > /home/user/data/beta/b.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

