FROM unix101-base:latest

USER root
RUN echo -e 'abcdefghij\nkilogram\n1234567890' > /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

