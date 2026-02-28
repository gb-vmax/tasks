FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/ls_test
RUN touch /home/user/ls_test/file1.txt
RUN touch /home/user/ls_test/.hiddenfile
RUN touch /home/user/ls_test/file2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

