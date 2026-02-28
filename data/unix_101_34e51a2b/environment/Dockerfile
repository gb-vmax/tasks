FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/notes
RUN echo -e 'Buy milk\nWalk the dog\nCall mom' > /home/user/notes/todo.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

