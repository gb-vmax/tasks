FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '# Custom dircolors file\nNORMAL 00\nDIR 01;34\n' > /home/user/custom_colors.conf
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

