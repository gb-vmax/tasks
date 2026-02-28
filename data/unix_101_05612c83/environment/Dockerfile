FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dir1 /home/user/dir2
RUN echo -e 'foo bar\nhello   world\nline3' > /home/user/dir1/test1.txt
RUN echo -e 'foo   bar\nhello world\nline3' > /home/user/dir2/test1.txt
RUN echo -e 'abc\ndef' > /home/user/dir1/test2.txt
RUN echo -e 'abc\ndef' > /home/user/dir2/test2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

