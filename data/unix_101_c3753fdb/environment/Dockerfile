FROM unix101-base:latest

USER root
RUN echo -ne 'line1\nline2\nline3\n' > /home/user/data.txt
RUN rm -f /home/user/second_line.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

