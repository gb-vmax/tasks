FROM unix101-base:latest

USER root
RUN printf "Sample A\n" > /home/user/filea.txt
RUN printf "Sample B\n" > /home/user/fileb.txt
RUN sha256sum /home/user/filea.txt > /home/user/files.sha256
RUN sha256sum /home/user/fileb.txt >> /home/user/files.sha256
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

