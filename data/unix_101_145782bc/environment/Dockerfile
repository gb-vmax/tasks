FROM unix101-base:latest

USER root
RUN echo -n 'Hello, this is a test file.' > /home/user/input.txt
RUN rm -f /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

