FROM unix101-base:latest

USER root
RUN echo -e 'hello world\nthis is a test' > /home/user/doc1.txt
RUN echo -e 'another test file\nwith more words' > /home/user/doc2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

