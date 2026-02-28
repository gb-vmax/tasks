FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'Report Title: Performance\n----------------------\nCPU Usage: 15%\nMemory Usage: 40%' > /home/user/data/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

