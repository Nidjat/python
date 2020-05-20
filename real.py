import consul

c = consul.Consul()

# poll a key for updates
index = 428
while True:
    index, data = c.kv.get('maximus', index=index)
    print data['22']
