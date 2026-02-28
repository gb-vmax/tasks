FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN printf '\xDE\xAD\xBE\xEF\x01\x23\x45\x67\x89\xAB\xCD\xEF' > /home/user/data/sample.bin
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

