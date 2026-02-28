FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN cat > /home/user/people.csv <<EOF
Name,Department,Salary
Jane,Engineering,85000
Mark,Design,76000
Sue,Marketing,68000
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

