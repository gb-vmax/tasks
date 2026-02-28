FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/input.txt <<EOF
First line

Second line


Third line
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

