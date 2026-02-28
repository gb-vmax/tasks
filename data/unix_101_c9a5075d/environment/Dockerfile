FROM unix101-base:latest

USER root
RUN printf '/home/user/project/file1.txt\n/home/user/project/subdir/file2.log\n/home/user/image.png\n' > /home/user/multi_paths.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

