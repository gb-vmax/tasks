FROM unix101-base:latest

USER root
RUN echo 'hello' > /home/user/a.txt
RUN echo 'world' > /home/user/b.txt
RUN printf 'a.txt\nb.txt\n' > /home/user/filelist.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

