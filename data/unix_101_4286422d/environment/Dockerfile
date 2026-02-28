FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'apple\nbanana\ncarrot\ndate' > /home/user/doc1.txt
RUN echo -e 'apple\nbanana\ncabbage\ndate' > /home/user/doc2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

