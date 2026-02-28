FROM unix101-base:latest

USER root
RUN echo 'A' > /home/user/alpha.txt
RUN echo 'B' >> /home/user/alpha.txt
RUN echo 'C' >> /home/user/alpha.txt
RUN echo '1' > /home/user/beta.txt
RUN echo '2' >> /home/user/beta.txt
RUN echo '3' >> /home/user/beta.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

