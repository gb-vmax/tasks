FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dir
RUN echo 'Log entry one' > /home/user/dir/file1.log
RUN echo 'Second log entry' > /home/user/dir/file2.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

