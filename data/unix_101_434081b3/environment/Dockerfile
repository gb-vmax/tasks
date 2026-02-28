FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs/subdir1
RUN mkdir -p /home/user/docs/subdir2
RUN echo 'Hello world' > /home/user/docs/file1.txt
RUN echo 'Another file' > /home/user/docs/file2.md
RUN echo 'Subdir text' > /home/user/docs/subdir1/notes.txt
RUN echo 'Ignore me' > /home/user/docs/subdir2/other.doc
RUN echo 'More text' > /home/user/docs/subdir2/readme.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

