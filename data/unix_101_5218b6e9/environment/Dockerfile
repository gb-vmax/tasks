FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testdir/subdir
RUN touch /home/user/testdir/fileA.txt
RUN touch /home/user/testdir/fileB.txt
RUN touch /home/user/testdir/subdir/fileC.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

