FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo -e "    This is line one\n        This is line two\n  Another indented line\nNoIndentHere" > /home/user/docs/indented.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

