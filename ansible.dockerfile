FROM ansible/ansible:ubuntu1404

RUN apt-get update -y && apt-get install -y wget libxml2-dev libxslt-dev libssl-dev libffi-dev \
    openssl &&\
    wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-2-amd64.deb &&\
    dpkg -i couchbase-release-1.0-2-amd64.deb &&\
    apt-get update -y && apt-get install -y libcouchbase-dev build-essential python-dev python-pip &&\
    pip install ansible couchbase &&\
    pip install ncclient junos-eznc xmljson &&\
    ansible-galaxy install Juniper.junos

WORKDIR /ansible

