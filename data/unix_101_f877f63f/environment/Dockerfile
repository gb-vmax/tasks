FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/animals.txt <<EOF
cat
cat
dog
dog
dog
bird
cat
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

