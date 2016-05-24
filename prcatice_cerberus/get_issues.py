import cerberus
schema = {'name':{'type':'string'}, 'age':{'type':'integer', 'min': 10}}
document = {'name': 1337, 'age': 5}
v = cerberus.Validator()
print(v.validate(document, schema))
print(v.errors)
document = {'name': 'john doe'}
print(v(document))