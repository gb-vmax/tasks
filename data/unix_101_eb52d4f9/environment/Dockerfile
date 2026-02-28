FROM unix101-base:latest

USER root
RUN dd if=/dev/zero bs=1 count=3000 status=none | tr '\0' 'A' > /home/user/bigfile.bin
RUN rm -f /home/user/limited_copy.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

