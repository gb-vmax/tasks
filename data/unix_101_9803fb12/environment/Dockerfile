FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'This is a line.' > /home/user/input.txt
RUN rm -f /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

