FROM unix101-base:latest

USER root
RUN printf 'apple\nbanana\ncarrot\n' > /home/user/file1.txt
RUN printf 'apple\nbanana\ncarrots\n' > /home/user/file2.txt
RUN gzip -c /home/user/file1.txt > /home/user/file1.txt.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

