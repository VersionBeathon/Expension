from transaction.tests.examples import DataManager
dm = DataManager()
print(dm.state)
print(dm.delta)
dm.inc()
print(dm.delta)
print(dm.state)
t1 = '1'
dm.prepare(t1)
print(dm.state)
dm.commit(t1)
print(dm.delta)

