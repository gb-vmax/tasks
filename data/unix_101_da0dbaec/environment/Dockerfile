FROM unix101-base:latest

USER root
RUN printf 'This is a sample line of text that is quite long and should be wrapped properly.\nAnotherlinewithnospacesandverylong.\nShort.\n' > /home/user/text.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

