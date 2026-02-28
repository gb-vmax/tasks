FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN echo 'main() {}' > /home/user/project/src/main.c
RUN echo 'README' > /home/user/project/README.md
RUN chmod 600 /home/user/project/src/main.c
RUN chmod 644 /home/user/project/README.md
RUN touch -t 202001011200 /home/user/project/src/main.c
RUN touch -t 202001011300 /home/user/project/README.md
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

