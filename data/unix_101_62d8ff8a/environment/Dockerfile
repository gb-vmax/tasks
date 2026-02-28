FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/source_dir/sub
RUN echo 'file a' > /home/user/source_dir/a.txt
RUN echo 'file b' > /home/user/source_dir/sub/b.txt
RUN chmod 700 /home/user/source_dir/a.txt
RUN chmod 600 /home/user/source_dir/sub/b.txt
RUN touch -t 202101010101 /home/user/source_dir/a.txt
RUN touch -t 202102020202 /home/user/source_dir/sub/b.txt
RUN rm -rf /home/user/backup_dir
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

