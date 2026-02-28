FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf 'Good line\nBad \xff line\nEnd\n' > /home/user/broken.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

