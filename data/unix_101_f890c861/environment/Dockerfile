FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'apple\nbanana\ncherry' > /home/user/data/alpha.txt
RUN echo -e 'apple\nbanana\norange' > /home/user/data/beta.txt
RUN gzip -c /home/user/data/alpha.txt > /home/user/data/alpha.txt.gz
RUN gzip -c /home/user/data/beta.txt > /home/user/data/beta.txt.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

