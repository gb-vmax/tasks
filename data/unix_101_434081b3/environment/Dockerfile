FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/documents/reports
RUN echo 'Report Q1' > /home/user/documents/reports/q1.txt
RUN echo 'Report Q2' > /home/user/documents/reports/q2.txt
RUN echo 'Notes' > /home/user/documents/notes.txt
RUN echo 'Not a text file' > /home/user/documents/data.csv
RUN touch /home/user/documents/reports/summary.docx
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

