import sys

from saba.client import SabaClient
from saba.auth.certificate import CertificateAuthentication

host = 'dimensiondatasb-api.sabacloud.com'
user = sys.argv[1]
password = sys.argv[2]

cert = CertificateAuthentication(host, user, password)

client = SabaClient(host, cert)

print(client.courses.all())