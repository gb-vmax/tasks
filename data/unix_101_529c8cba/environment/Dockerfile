FROM unix101-base:latest

USER root
RUN printf "Alpha file contents\n" > /home/user/alpha.txt
RUN printf "Beta test contents\n" > /home/user/beta.txt
RUN md5sum /home/user/alpha.txt > /home/user/checksums.md5
RUN md5sum /home/user/beta.txt >> /home/user/checksums.md5
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

