FROM unix101-base:latest

USER root
RUN echo 'Hello, ACL world!' > /home/user/testfile.txt
RUN setfacl -m u:user:rw /home/user/testfile.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

