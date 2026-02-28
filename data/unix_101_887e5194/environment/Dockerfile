FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/customman
RUN echo 'foo manpage' > /home/user/customman/foo.1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

