FROM unix101-base:latest

USER root
RUN echo 'Example data for bunzip2.' > /home/user/data.txt
RUN bzip2 /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

