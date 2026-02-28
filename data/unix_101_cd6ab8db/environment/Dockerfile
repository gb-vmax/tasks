FROM unix101-base:latest

USER root
RUN echo 'aaa' > /home/user/a1.o
RUN echo 'bbb' > /home/user/a2.o
RUN echo 'ccc' > /home/user/a3.o
RUN ar rcs /home/user/libmulti.a /home/user/a1.o /home/user/a2.o /home/user/a3.o
RUN rm -f /home/user/a1.o /home/user/a2.o /home/user/a3.o
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

