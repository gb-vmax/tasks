FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'id,name,score
1,Alice,85
2,Bob,92' > /home/user/data/report.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

