FROM unix101-base:latest

USER root
RUN echo -e 'apple\napplejack\napricot\nbanana\napex\napply\nape\nmaple' > /home/user/words.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

