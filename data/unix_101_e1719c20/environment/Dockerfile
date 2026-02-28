FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo 'The quick brown fox jumps over the lazy dog.' > /home/user/doc1.txt
RUN echo 'The quick red fox jumps over the lazy dog.' > /home/user/doc2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

