FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN touch /home/user/docs/notes.txt
RUN touch /home/user/docs/todo.txt
RUN touch /home/user/docs/readme.txt
RUN touch /home/user/docs/manual.md
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

