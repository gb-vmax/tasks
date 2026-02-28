FROM unix101-base:latest

USER root
RUN printf "Header info\n=== SESSION START ===\nUser: Alice\nAction: Login\n=== SESSION START ===\nUser: Bob\nAction: Logout\n=== SESSION START ===\nUser: Eve\nAction: Login\n" > /home/user/server.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

