FROM unix101-base:latest

USER root
RUN ip link add veth1 type veth peer name veth2
RUN ip addr add 10.10.10.1/24 dev veth1
RUN ip addr add 10.10.10.2/24 dev veth2
RUN ip link set veth1 up
RUN ip link set veth2 up
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

