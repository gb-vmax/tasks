FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'Hello\nWorld\nBye' > /home/user/base.txt
RUN echo -e 'Hello\nWorld!\nBye' > /home/user/theirs.txt
RUN echo -e 'Hello\nWorld\nGoodbye' > /home/user/yours.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

