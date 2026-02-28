FROM unix101-base:latest

USER root
RUN printf "This is an info message\nThis is an error message\nAnother line\nerror: file not found\nNo issues detected\n" > /home/user/logfile.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

