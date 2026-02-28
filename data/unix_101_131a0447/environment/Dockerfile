FROM unix101-base:latest

USER root
RUN rm -f /home/user/greet_alias.txt
RUN echo '' > /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

