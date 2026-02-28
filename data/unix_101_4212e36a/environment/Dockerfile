FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/files
RUN echo 'data file' > /home/user/data/files/myfile.txt
RUN mkdir -p /home/user/links
RUN ln -s /home/user/data/files/myfile.txt /home/user/links/myfile_symlink
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

