FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/data.txt <<EOF
Name Age City
Alice 30 Boston
Bob 25 Seattle
Carol 22 Miami
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

