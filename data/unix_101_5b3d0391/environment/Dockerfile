FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/colors.txt <<EOF
Red
red
RED
blue
Blue
green
Green
green
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

