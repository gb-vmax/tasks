FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN dd if=/dev/zero bs=1 count=5000 of=/home/user/largefile.bin status=none
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

