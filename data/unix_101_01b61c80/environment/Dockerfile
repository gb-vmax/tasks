FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN printf '\x44\x61\x74\x61\x31\x32\x33' > /home/user/binfile_original.bin
RUN xxd /home/user/binfile_original.bin /home/user/binfile.hex
RUN rm /home/user/binfile_original.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

