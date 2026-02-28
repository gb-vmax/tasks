FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'apple\nbanana\ncherry' > /home/user/data/col1.txt
RUN echo -e 'red\nyellow\npurple' > /home/user/data/col2.txt
RUN rm -f /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

