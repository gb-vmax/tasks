FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testdir
RUN echo 'data1' > /home/user/testdir/file1.txt
RUN echo 'data2' > /home/user/testdir/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

