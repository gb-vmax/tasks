FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/subdir
RUN echo 'Alpha' > /home/user/fileA.txt
RUN echo 'Bravo' > /home/user/subdir/fileB.txt
RUN echo 'Charlie' > /home/user/fileC.txt
RUN cd /home/user
RUN printf 'fileA.txt\nsubdir/fileB.txt\nfileC.txt\n' | cpio -o -c > myarchive.cpio
RUN echo 'subdir/fileB.txt' > /home/user/patterns.txt
RUN rm -f /home/user/subdir/fileB.txt
RUN rm -f /home/user/fileA.txt
RUN rm -f /home/user/fileC.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

