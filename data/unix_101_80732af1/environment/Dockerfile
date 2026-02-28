FROM unix101-base:latest

USER root
RUN cd /home/user
RUN mkdir -p src
RUN echo 'print("Test")' > src/test.py
RUN echo '# Project README' > README.md
RUN zip -r project.zip src/ README.md
RUN rm -r src README.md
RUN mkdir -p extracted
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

