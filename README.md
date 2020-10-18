# IpToHostname

Elimizdeki ip listesinden subdomain adreslerini bulmak için yapılmış basit bir programdır.

# Install

```
pip3 install -r requirements.txt
```
# Usage

```
python3 IpToHostname.py --list /path/ip-address-list.txt --target paypal.com 

```

# Mantık

program ip adreslerini sırası ile https://www.ip-tracker.org/ web sitesinde sorgular. Eğer response da --target parametresi ile belirttiğiniz domaine ait iz bulunursa, ip adresi ile subdomain adresi ekrana bastırılır.
