FROM unix101-base:latest

USER root
RUN echo 'Temporary content.' > /home/user/tmpfile.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

