FROM unix101-base:latest

USER root
RUN printf 'ABCDE12345FGHIJ' > /home/user/alpha.bin
RUN printf 'ABCDE12345FGHIJ' > /home/user/beta.bin
RUN dd if=/home/user/beta.bin of=/home/user/beta.bin conv=notrunc bs=1 seek=5 count=5 <<< 'XXXXX'
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

