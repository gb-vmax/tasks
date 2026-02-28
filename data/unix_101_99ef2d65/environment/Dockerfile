FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '\x01\x02\x03\x04\x05\x06\x07\x08' > /home/user/old_data.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

