FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/files
RUN echo -e "1000\n2500000\n999999" > /home/user/files/sizes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

