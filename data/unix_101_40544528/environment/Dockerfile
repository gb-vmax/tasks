FROM unix101-base:latest

USER root
RUN echo -e 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6' > /home/user/doc.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

