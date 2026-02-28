FROM unix101-base:latest

USER root
RUN echo 'line one' > /home/user/left.txt
RUN echo 'line two' >> /home/user/left.txt
RUN echo 'line three' >> /home/user/left.txt
RUN echo 'line four' >> /home/user/left.txt
RUN echo 'line one' > /home/user/right.txt
RUN echo 'line two changed' >> /home/user/right.txt
RUN echo 'line three' >> /home/user/right.txt
RUN echo 'line four extra' >> /home/user/right.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

