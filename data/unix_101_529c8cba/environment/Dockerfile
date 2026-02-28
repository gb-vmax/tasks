FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/files
RUN echo 'apple' > /home/user/files/file1.txt
RUN echo 'banana' > /home/user/files/file2.txt
RUN md5sum /home/user/files/file1.txt > /home/user/files/MD5SUMS
RUN md5sum /home/user/files/file2.txt >> /home/user/files/MD5SUMS
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

