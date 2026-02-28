FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN mkdir -p /home/user/project/tests/unit
RUN touch /home/user/project/README.md
RUN touch /home/user/project/src/main.py
RUN touch /home/user/project/src/utils.py
RUN touch /home/user/project/tests/test_main.py
RUN touch /home/user/project/tests/unit/test_utils.py
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

