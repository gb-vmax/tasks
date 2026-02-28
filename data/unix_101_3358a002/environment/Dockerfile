FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/subdir
RUN echo 'main code' > /home/user/project/code.py
RUN echo 'subdir note' > /home/user/project/subdir/note.txt
RUN setfacl -m u:1001:rw- /home/user/project/code.py
RUN setfacl -m g:1002:r-- /home/user/project/subdir/note.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

