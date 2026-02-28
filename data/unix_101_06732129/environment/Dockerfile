FROM unix101-base:latest

USER root
RUN echo 'This is a note.' > /home/user/note.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

