FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN date -d '2023-08-15' +'%Y-%m-%d' > /home/user/fixed-date.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

