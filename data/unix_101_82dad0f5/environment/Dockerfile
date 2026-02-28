FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN ip link add dummy0 type dummy
RUN ip addr add 192.168.1.10/24 dev dummy0
RUN ip link set dummy0 up
RUN arp -s 192.168.1.20 00:11:22:33:44:55 -i dummy0
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

