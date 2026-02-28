FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'John Doe' > /home/user/name.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

