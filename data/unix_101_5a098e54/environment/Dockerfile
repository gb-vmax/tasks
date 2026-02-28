FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/documents
RUN touch /home/user/documents/report2024.pdf
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

