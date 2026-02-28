FROM unix101-base:latest

USER root
RUN printf '{"id": 1, "name": "Alice"}\n' > /home/user/user1.json
RUN printf '{"id": 2, "name": "Bob"}\n' > /home/user/user2.json
RUN printf '{"id": 3, "name": "Charlie"}\n' > /home/user/user3.json
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

