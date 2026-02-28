FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Annual Report 2023\nSummary: Profits increased.' > /home/user/docs/report.txt
RUN xz /home/user/docs/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

