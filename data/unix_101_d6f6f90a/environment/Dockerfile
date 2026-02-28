FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/dirA
RUN mkdir -p /home/user/data/dirB
RUN touch /home/user/data/fileA.txt
RUN touch /home/user/data/fileB.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

