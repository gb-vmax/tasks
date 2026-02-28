FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/notes
RUN cat > /home/user/notes/todo.txt <<EOF
[ ] Buy milk
[x] Call Alice
[ ] Read book
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

