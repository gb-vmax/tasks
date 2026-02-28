FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs/subdir
RUN echo 'File A' > /home/user/docs/a.txt
RUN echo 'File B' > /home/user/docs/b.txt
RUN echo 'Subdir File' > /home/user/docs/subdir/c.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

