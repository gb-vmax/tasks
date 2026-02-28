FROM unix101-base:latest

USER root
RUN printf "liba libc\nlibb libc\nlibc libd\nlibe libd\nlibf libe\n" > /home/user/input.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

