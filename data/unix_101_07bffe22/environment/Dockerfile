FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project
RUN mkdir -p /home/user/docs
RUN printf "Project Introduction\n" > /home/user/project/intro.txt
RUN printf "Project Summary\n" > /home/user/project/summary.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

