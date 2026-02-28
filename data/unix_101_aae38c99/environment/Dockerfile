FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dir1 /home/user/dir2 /home/user/dir3
RUN echo 'apple' > /home/user/dir1/fileA.txt
RUN echo 'banana' > /home/user/dir2/fileB.txt
RUN echo 'cherry' > /home/user/dir3/fileC.txt
RUN tar -cf /home/user/all_dirs.tar -C /home/user dir1 dir2 dir3
RUN rm -rf /home/user/dir1 /home/user/dir2 /home/user/dir3
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

