FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project_backup/src
RUN echo 'main.c contents' > /home/user/project_backup/src/main.c
RUN echo 'README' > /home/user/project_backup/README.md
RUN touch /home/user/project_backup/.env
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

