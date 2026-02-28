FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data/folder1
RUN mkdir -p /home/user/data/folder2
RUN echo 'Alpha' > /home/user/data/fileA.txt
RUN echo 'Beta' > /home/user/data/folder1/fileB.txt
RUN echo 'Gamma' > /home/user/data/folder2/fileC.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

