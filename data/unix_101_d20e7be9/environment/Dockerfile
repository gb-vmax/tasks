FROM unix101-base:latest

USER root
RUN printf "This is the source file.\n" > /home/user/source.txt
RUN rm -f /home/user/destination.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

