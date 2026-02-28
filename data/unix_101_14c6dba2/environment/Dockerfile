FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/projectA/subdir
RUN echo 'Main file' > /home/user/projectA/file1.txt
RUN echo 'Subdirectory file' > /home/user/projectA/subdir/file2.txt
RUN mkdir -p /home/user/projectB/subdir
RUN echo 'Old file' > /home/user/projectB/old.txt
RUN echo 'To be replaced' > /home/user/projectB/file1.txt
RUN echo 'Extraneous' > /home/user/projectB/subdir/extra.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

