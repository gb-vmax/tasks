FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN rm -f /home/user/ignored_proc.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

