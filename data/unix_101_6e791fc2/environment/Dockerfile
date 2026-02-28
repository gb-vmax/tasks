FROM unix101-base:latest

USER root
RUN echo 'Sample data for checksum.' > /home/user/testdata.txt
RUN rm -f /home/user/checksums.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

