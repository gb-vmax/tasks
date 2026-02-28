FROM unix101-base:latest

USER root
RUN echo 'export FOO=bar' >> /etc/profile
RUN echo 'export BAZ=qux' >> /etc/profile
RUN mkdir -p /home/user
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

