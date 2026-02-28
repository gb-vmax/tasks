FROM unix101-base:latest

USER root
RUN echo -e 'Meeting notes:\n- Item 1\n- Item 2\n- Item 3' > /home/user/notes.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

