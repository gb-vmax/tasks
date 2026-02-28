FROM unix101-base:latest

USER root
RUN echo 'object content 1' > /home/user/foo.o
RUN echo 'object content 2' > /home/user/bar.o
RUN rm -f /home/user/libstuff.a
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

