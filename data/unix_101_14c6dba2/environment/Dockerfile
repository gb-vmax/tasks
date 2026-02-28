FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project_src
RUN echo 'build ok' > /home/user/project_src/build.log
RUN echo 'run ok' > /home/user/project_src/run.log
RUN echo 'main code' > /home/user/project_src/main.py
RUN echo 'README' > /home/user/project_src/README.md
RUN mkdir -p /home/user/project_backup
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

