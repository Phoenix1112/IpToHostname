# IpToHostname

elimizde ip adreslerinden oluşan bir liste olduğu varsayıyoruz. Bu ip adreslerinin hangisi paypal.com'a ait subdomaine ait olup olmadığını bulmak için bu programı kullanabilirsiniz.

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
