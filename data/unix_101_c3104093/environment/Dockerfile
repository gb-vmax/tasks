FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo 'First log entry' > /home/user/logs/log1.txt
RUN echo 'Second log entry' > /home/user/logs/log2.txt
RUN bzip2 -k /home/user/logs/log1.txt
RUN bzip2 -k /home/user/logs/log2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

