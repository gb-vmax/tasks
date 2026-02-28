FROM unix101-base:latest

USER root
RUN ip link add veth1 type veth peer name veth2
RUN ip link set veth1 up
RUN ip link set veth2 up
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

