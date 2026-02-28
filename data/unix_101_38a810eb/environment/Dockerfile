FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN echo 'Old file' > /home/user/project/old.txt
RUN sleep 1
RUN echo 'New file' > /home/user/project/new.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

