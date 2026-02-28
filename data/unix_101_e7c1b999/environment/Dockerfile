FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/subdir
RUN echo 'abc' > /home/user/project/file1.txt
RUN head -c 2048 /dev/zero > /home/user/project/file2.bin
RUN echo 'hello world' > /home/user/project/subdir/file3.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

