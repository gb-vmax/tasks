FROM unix101-base:latest

USER root
RUN echo -e 'cat\ndog\nbird\nfrog\nlion\ntiger\ncatfish\ndogma' > /home/user/animals.txt
RUN echo -e 'cat\ndog' > /home/user/patterns.txt
RUN rm -f /home/user/match_count.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

