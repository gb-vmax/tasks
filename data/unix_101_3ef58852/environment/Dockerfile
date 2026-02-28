FROM unix101-base:latest

USER root
RUN echo -e 'A1\nA2\nA3' > /home/user/alpha.txt
RUN echo -e 'B1\nB2' > /home/user/beta.txt
RUN rm -f /home/user/merged.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

