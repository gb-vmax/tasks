FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN mkdir -p /home/user/docs
RUN echo "2024 Q2 Report" > /home/user/data/report.txt
RUN ln -s ../data/report.txt /home/user/docs/shortcut.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

