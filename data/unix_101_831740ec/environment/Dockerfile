FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/unportable
RUN touch /home/user/unportable/normal.txt
RUN touch /home/user/unportable/verylongfilenameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.txt
RUN touch /home/user/unportable/file_with:colon.txt
RUN touch /home/user/unportable/-leadingdash.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

