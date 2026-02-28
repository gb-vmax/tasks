FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN echo 'SHA1 checksum verification example.' > /home/user/project/readme.md
RUN echo 'f1c1b3a3b1f8b3a0fa6c8e4c4e849eea2cbf3ca4  readme.md' > /home/user/project/readme.sha1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

