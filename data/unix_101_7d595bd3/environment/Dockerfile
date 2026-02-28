FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/dir
RUN printf 'line1\nline2\nline3\nuniqueA\nend\n' > /home/user/dir/dataA
RUN printf 'line1\nline2\nline3\nuniqueB\nend\n' > /home/user/dir/dataB
RUN gzip -c /home/user/dir/dataA > /home/user/dir/dataA.gz
RUN gzip -c /home/user/dir/dataB > /home/user/dir/dataB.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

