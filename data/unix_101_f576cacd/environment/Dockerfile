FROM unix101-base:latest

USER root
RUN printf 'Line1\\nLine2\\tTabbed\\nEnd' > /home/user/input.txt
RUN rm -f /home/user/result.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

