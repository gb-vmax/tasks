FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN ip link add dummy1 type dummy
RUN ip addr add 10.10.10.1/24 dev dummy1
RUN ip link set dummy1 up
RUN echo '10.10.10.2 00:aa:bb:cc:dd:ee' > /home/user/arp_entries.txt
RUN echo '10.10.10.3 00:11:22:33:44:66' >> /home/user/arp_entries.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

