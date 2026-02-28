FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Project documentation' > /home/user/docs/readme.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

