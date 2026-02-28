FROM unix101-base:latest

USER root
RUN echo 'Archive content for bunzip2 test.' > /home/user/archive
RUN bzip2 /home/user/archive
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

