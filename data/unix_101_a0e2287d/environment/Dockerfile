FROM unix101-base:latest

USER root
RUN printf '{"name": "Alice", "age": 30, "city": "Wonderland"}\n' > /home/user/data.json
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

