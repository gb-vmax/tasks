FROM unix101-base:latest

USER root
RUN printf "This is a long paragraph in a file that needs to be reformatted. Each sentence should not exceed the specified width after formatting. This is for testing the fmt command.\n" > /home/user/text1.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

