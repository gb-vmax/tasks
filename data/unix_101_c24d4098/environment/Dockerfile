FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/subdir
RUN printf 'abcdefg' > /home/user/project/file1.txt
RUN printf '1234567890' > /home/user/project/subdir/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

