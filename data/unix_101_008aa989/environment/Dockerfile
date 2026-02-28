FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/temp_dir/subdir
RUN echo 'Temporary file 1' > /home/user/temp_dir/file1.txt
RUN echo 'Temporary file 2' > /home/user/temp_dir/subdir/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

