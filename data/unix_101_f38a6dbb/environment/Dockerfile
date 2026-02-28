FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '\x00\x01\x02Hello\x00World!\x03\x04TEST1234\x00' > /home/user/binfile.dat
RUN rm -f /home/user/strings.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

