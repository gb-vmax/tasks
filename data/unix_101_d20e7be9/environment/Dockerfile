FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/targetdir
RUN echo 'Hello World' > /home/user/source1.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

