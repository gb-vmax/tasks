FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "1234567890abcdef" > /home/user/file1.bin
RUN printf "XYZ" > /home/user/file2.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

