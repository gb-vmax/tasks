FROM unix101-base:latest

USER root
RUN printf "Charlie\nAlice\nBob\nEve\nDavid\n" > /home/user/names.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

