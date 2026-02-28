FROM unix101-base:latest

USER root
RUN printf "1,Alice,25\n2,Bob,30\n3,Carol,28\n4,David,22\n" > /home/user/people.csv
RUN printf "NY,New York\nLA,Los Angeles\nSF,San Francisco\nBob,Chicago\nCarol,Denver\nDavid,Houston\n" > /home/user/cities.csv
RUN sort -t, -k2,2 /home/user/people.csv -o /home/user/people.csv
RUN sort -t, -k1,1 /home/user/cities.csv -o /home/user/cities.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

