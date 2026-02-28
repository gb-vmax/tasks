FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/subdir
RUN echo 'main file' > /home/user/project/main.txt
RUN echo 'sub content' > /home/user/project/subdir/sub.txt
RUN tar -cf /home/user/project.tar -C /home/user/project .
RUN mkdir -p /home/user/output
RUN rm -rf /home/user/project
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

