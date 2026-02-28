FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN ip link add eth0 type dummy || true
RUN ip link set eth0 up || true
RUN ip link set eth0 mtu 1500 || true
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

