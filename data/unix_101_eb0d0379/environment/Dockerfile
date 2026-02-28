FROM unix101-base:latest

USER root
RUN echo 'Hello world' > /home/user/file1.txt
RUN echo 'Testing tar' > /home/user/file2.txt
RUN echo 'Do not include me' > /home/user/file3.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

