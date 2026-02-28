FROM unix101-base:latest

USER root
RUN rm -rf /home/user/*
RUN touch /home/user/colors.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

