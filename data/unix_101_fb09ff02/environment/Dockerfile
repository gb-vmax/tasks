FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/data.csv <<EOF
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Carol,28,Chicago
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

