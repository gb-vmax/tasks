FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/archive
RUN echo 'data1' > /home/user/data/file1.txt
RUN echo 'data2' > /home/user/data/file2.txt
RUN echo 'archived data' > /home/user/data/archive/file3.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

