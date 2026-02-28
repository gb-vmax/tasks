FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN echo 'Old content' > /home/user/greeting.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

