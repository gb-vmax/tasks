FROM unix101-base:latest

USER root
RUN echo -e '1 Alice\n2 Bob\n3 Carol' > /home/user/people.txt
RUN echo -e '1 London\n2 Paris\n3 Berlin' > /home/user/cities.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

