FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -n 'SECRET-DATA-12345' > /home/user/data.bin
RUN sha256sum /home/user/data.bin > /home/user/data.sha256
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

