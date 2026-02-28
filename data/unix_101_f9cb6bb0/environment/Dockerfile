FROM unix101-base:latest

USER root
RUN echo -e '101,Apple\n102,Banana\n103,Orange' > /home/user/products.csv
RUN echo -e '101,1.20\n103,0.80\n104,2.00' > /home/user/prices.csv
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

