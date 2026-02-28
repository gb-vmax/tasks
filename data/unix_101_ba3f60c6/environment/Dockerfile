FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/code
RUN echo -e "    a    b    c\n        indented\n  mid  spaces\nno_spaces" > /home/user/code/spaces.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

