FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '\x10\x20AB\x00CDEFG\x00H\x00XY\x00' > /home/user/mixedbytes.bin
RUN rm -f /home/user/short_strings.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

