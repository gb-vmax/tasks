FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/texts
RUN echo -e 'This is a line that should wrap.
Short.' > /home/user/texts/shorttext.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

