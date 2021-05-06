FROM ubuntu

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy && \
    pip3 install -i https://test.pypi.org/simple/ lambdata-minh-0.0.2


WORKDIR /lambdata_minh/
COPY . /lambdata_minh/

