FROM unix101-base:latest

USER root
RUN echo Banana > /home/user/fruits.txt
RUN echo Apple >> /home/user/fruits.txt
RUN echo Cherry >> /home/user/fruits.txt
RUN echo Date >> /home/user/fruits.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

