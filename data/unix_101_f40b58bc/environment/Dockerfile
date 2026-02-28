FROM unix101-base:latest

USER root
RUN printf "First line\nSecond line\nThird line\nFourth line\n" > /home/user/notes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

