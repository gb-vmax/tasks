FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'banana\napple\ncarrot' > /home/user/notes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

