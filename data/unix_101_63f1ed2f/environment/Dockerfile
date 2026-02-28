FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Meeting notes' > /home/user/docs/notes.txt
RUN echo 'Project plan' > /home/user/docs/plan.txt
RUN echo 'Readme' > /home/user/docs/readme.md
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

