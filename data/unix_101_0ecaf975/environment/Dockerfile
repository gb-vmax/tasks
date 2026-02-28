FROM unix101-base:latest

USER root
RUN printf "Name\tAge\tCity\nAlice\t30\tNew York\nBob\t25\tLos Angeles\nCharlie\t35\tChicago\nDiana\t28\tMiami\n" > /home/user/people.tsv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

