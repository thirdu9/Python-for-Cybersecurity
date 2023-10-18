
import dns
import dns.resolver
import socket

domain = 'www.google.com'

result = dns.resolver.resolve(domain, 'A')
print(result)
for answer in result:
    print(answer)

addr = socket.gethostbyaddr(answer.to_text())

print([addr[0]]+addr[1])
