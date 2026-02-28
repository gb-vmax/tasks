FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN cat > /home/user/data/users.csv <<EOF
alice,alice@example.com,admin
bob,bob@example.com,user
carol,carol@example.com,guest
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

