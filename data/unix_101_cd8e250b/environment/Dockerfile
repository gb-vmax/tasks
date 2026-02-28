FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN printf '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0user1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0tty1\0\0\0\0\0\0\0\0\0\0\0\0host1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0' > /home/user/testutmp
RUN printf '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0user2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0tty2\0\0\0\0\0\0\0\0\0\0\0\0host2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0' >> /home/user/testutmp
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

