FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "hello world\nthis is a test file\nwith several lines\n" > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

