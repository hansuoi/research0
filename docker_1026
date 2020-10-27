 FROM ubuntu:latest

 RUN apt-get update && apt-get -y upgrade && \
     apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 \
 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 wget -y && \
     wget -P /opt https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh && \
     bash /opt/Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/anaconda3 && \
     rm /opt/Anaconda3-2020.02-Linux-x86_64.sh && \
     echo "export PATH=/opt/anaconda3/bin:$PATH" >> ~/.bashrc && \
     . ~/.bashrc && \
     conda init
