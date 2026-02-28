FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN mkdir -p /home/user/project/tests
RUN echo 'main code' > /home/user/project/src/main.py
RUN touch /home/user/project/src/empty1.py
RUN touch /home/user/project/src/empty2.py
RUN echo 'test code' > /home/user/project/tests/test_main.py
RUN touch /home/user/project/tests/empty_test.py
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

