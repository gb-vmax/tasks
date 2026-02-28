FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "id,name,score\n1,Alice,90\n2,Bob,85\n3,Carol,95\n" > /home/user/data.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

