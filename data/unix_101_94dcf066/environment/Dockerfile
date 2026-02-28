FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncarrot\n" > /home/user/data.txt
RUN gzip -c /home/user/data.txt > /home/user/data.txt.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

