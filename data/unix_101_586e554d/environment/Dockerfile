FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Hello World' > /home/user/docs/file1.txt
RUN echo 'Unix training' > /home/user/docs/file2.txt
RUN b2sum /home/user/docs/file1.txt > /home/user/filesums.txt
RUN b2sum /home/user/docs/file2.txt >> /home/user/filesums.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

