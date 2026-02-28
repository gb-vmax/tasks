FROM unix101-base:latest

USER root
RUN echo -e 'This is line one.\nThis is line two.\nThis is line three.' > /home/user/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

