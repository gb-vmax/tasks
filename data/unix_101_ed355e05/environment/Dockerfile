FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/source_dir
RUN echo 'alpha' > /home/user/source_dir/file1.txt
RUN echo 'beta' > /home/user/source_dir/file2.txt
RUN mkdir -p /home/user/dest_dir
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

