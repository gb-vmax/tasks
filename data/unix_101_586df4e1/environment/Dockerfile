FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/numbers.txt <<EOF
A 5 100
B 2 200
C 8 300
D 7 400
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

