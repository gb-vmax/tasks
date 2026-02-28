FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testdir
RUN touch /home/user/testdir/file1.txt
RUN touch /home/user/testdir/file2.txt
RUN echo 'data1' > /home/user/testdir/file1.txt
RUN echo 'data2' > /home/user/testdir/file2.txt
RUN chown -R user:user /home/user
RUN su - user -c 'tail -f /home/user/testdir/file1.txt > /dev/null 2>&1 &'
RUN sleep 1
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

