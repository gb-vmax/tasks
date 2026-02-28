FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "Meeting at 10am\nLunch at 1pm\n" > /home/user/notes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

