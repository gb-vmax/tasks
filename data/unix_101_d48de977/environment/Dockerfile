FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project_dir/subdir1
RUN mkdir -p /home/user/project_dir/subdir2
RUN printf 'file1 contents' > /home/user/project_dir/file1.txt
RUN printf 'file2 contents' > /home/user/project_dir/subdir1/file2.txt
RUN printf 'file3 contents' > /home/user/project_dir/subdir2/file3.txt
RUN chmod 600 /home/user/project_dir/file1.txt
RUN chmod 600 /home/user/project_dir/subdir1/file2.txt
RUN chmod 600 /home/user/project_dir/subdir2/file3.txt
RUN chmod 700 /home/user/project_dir
RUN chmod 700 /home/user/project_dir/subdir1
RUN chmod 700 /home/user/project_dir/subdir2
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

