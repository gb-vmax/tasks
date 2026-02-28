FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN rm -f /home/user/logs/alice_wtmp
RUN touch /home/user/logs/alice_wtmp
RUN chown -R user:user /home/user
RUN date1=$(date -d '2023-01-01 10:00:00' +%s)
RUN date2=$(date -d '2023-01-01 12:00:00' +%s)
RUN date3=$(date -d '2023-01-02 09:30:00' +%s)
RUN date4=$(date -d '2023-01-02 11:00:00' +%s)
RUN python3 -c 'import struct; import sys; f=open("/home/user/logs/alice_wtmp", "wb"); f.write(struct.pack("=hi32s4s32s256shhiii4i20s",2,0,b"alice",b"pts1",b":0",b"localhost",7,0,0,0,0,'"$date1"',"$date2",0,0,0,0,b"")); f.write(struct.pack("=hi32s4s32s256shhiii4i20s",2,0,b"alice",b"pts1",b":0",b"remotehost",7,0,0,0,0,'"$date3"',"$date4",0,0,0,0,b"")); f.close()')
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

