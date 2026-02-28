FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/env
RUN echo 'red:green:blue:yellow' > /home/user/env/colors.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

