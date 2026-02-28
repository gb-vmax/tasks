FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN cat > /home/user/data/prefixed.txt <<EOF
# This is a comment that should be wrapped to the specified width.
Normal text that should not be changed.
# Another comment that is also very long and should be wrapped nicely.
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

