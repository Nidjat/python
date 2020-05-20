import consul

c = consul.Consul()

# poll a key for updates
index = None
while True:
    index, data = c.kv.get('maximus', index=index)
    print(data['Value'])

