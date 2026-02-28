FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/archive
RUN printf 'id,name,score\n1,Alice,95\n2,Bob,88\n' > /home/user/archive/data.csv
RUN bzip2 /home/user/archive/data.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

