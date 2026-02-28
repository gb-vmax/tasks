FROM unix101-base:latest

USER root
RUN echo '{"name": "Alice", "email": "alice@example.com", "age": 29}' > /home/user/profile.json
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

