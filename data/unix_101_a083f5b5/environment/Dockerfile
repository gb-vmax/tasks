FROM unix101-base:latest

USER root
RUN echo 'Hello from file1' > /home/user/file1.txt
RUN echo 'Hello from file2' > /home/user/file2.txt
RUN printf 'file1.txt\nfile2.txt\n' > /home/user/filelist.txt
RUN rm -f /home/user/archive.cpio
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

