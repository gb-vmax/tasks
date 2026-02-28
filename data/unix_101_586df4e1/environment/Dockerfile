FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "Region\tProduct\tAmount\nEast\tPen\t120\nWest\tPencil\t90\nEast\tNotebook\t150\nWest\tPen\t110\n" > /home/user/sales.tsv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

