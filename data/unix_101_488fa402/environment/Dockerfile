FROM unix101-base:latest

USER root
RUN printf "This is a test of base64 line wrapping." > /home/user/raw.txt
RUN base64 -w 8 /home/user/raw.txt > /home/user/data.b64
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

