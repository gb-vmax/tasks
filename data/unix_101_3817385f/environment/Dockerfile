FROM unix101-base:latest

USER root
RUN echo 'Meeting at 3pm.' > /home/user/note.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

