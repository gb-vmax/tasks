FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN touch /home/user/project/file1.txt
RUN touch /home/user/project/.hidden1
RUN touch /home/user/project/.hidden2
RUN touch /home/user/project/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

