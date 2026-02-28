FROM unix101-base:latest

USER root
RUN rm -f /home/user/nums.txt
RUN mkdir -p /home/user
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

