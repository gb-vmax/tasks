FROM unix101-base:latest

USER root
RUN printf "first line\nsecond line\nthird line\n" > /home/user/data.txt
RUN gzip -c /home/user/data.txt > /home/user/data.txt.gz
RUN rm /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

