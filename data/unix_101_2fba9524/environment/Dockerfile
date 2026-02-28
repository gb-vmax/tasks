FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN mkdir -p /home/user/project/test
RUN touch /home/user/project/README.md
RUN touch /home/user/project/src/main.c
RUN touch /home/user/project/src/utils.c
RUN touch /home/user/project/test/test_main.c
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

