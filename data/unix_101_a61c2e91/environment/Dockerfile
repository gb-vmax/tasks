FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf '\x01\x02\x03\x04H\x65\x6c\x6c\x6f\n' > /home/user/data/binary.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

