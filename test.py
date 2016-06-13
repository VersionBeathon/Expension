d = {'title': 'python web site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items)
it = d.iteritems()
print(list(it))
x = {'title': 'baidulaji'}
d.update(x)
print(d)