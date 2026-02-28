FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/original
RUN ln -s /home/user/original /home/user/linkdir
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

