FROM unix101-base:latest

USER root
RUN echo 'Compression and decompression with zstd.' > /home/user/original.txt
RUN zstd /home/user/original.txt -o /home/user/archive.zst
RUN rm /home/user/original.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

