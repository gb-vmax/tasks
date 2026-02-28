FROM unix101-base:latest

USER root
RUN echo 'Hello World' > /home/user/file1.txt
RUN echo 'Goodbye World' > /home/user/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

