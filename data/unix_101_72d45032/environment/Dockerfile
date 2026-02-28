FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testdata
RUN echo 'Unsaved data' > /home/user/testdata/file1.txt
RUN echo 'More unsaved data' > /home/user/testdata/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

