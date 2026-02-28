FROM unix101-base:latest

USER root
RUN echo 'greet() { echo "Hello, Unix!"; }' >> /home/user/.bashrc
RUN echo 'greet() { echo "Hello, Unix!"; }' > /home/user/funcsetup.sh
RUN echo 'greet > /home/user/greet_output_before.txt' >> /home/user/funcsetup.sh
RUN chmod +x /home/user/funcsetup.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

