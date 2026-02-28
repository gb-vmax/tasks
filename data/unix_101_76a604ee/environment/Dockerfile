FROM unix101-base:latest

USER root
RUN echo -e 'Charlie\nAlice\nEve\nBob' > /home/user/names.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

