FROM unix101-base:latest

USER root
RUN printf '00000000: 4865 6c6c 6f2c 2055 6e69 7821 0a         Hello, Unix!\n' > /home/user/dump.hex
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

