FROM unix101-base:latest

USER root
RUN echo 'Hello, world!' > /home/user/file1.txt
RUN rm -f /home/user/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

