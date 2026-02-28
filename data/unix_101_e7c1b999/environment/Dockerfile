FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/data
RUN echo 'Hello World' > /home/user/project/file1.txt
RUN echo 'Another file' > /home/user/project/file2.txt
RUN echo 'Some data' > /home/user/project/data/data1.txt
RUN echo 'More data' > /home/user/project/data/data2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

