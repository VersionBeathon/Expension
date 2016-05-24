from transaction.tests.examples import DataManager
dm = DataManager()
dm.inc()
print(dm.state, dm.delta)
t1 = '1'
dm.abort(t1)
print(dm.state, dm.delta)

dm.inc()
r = dm.savepoint(t1)
dm.inc()
r = dm.savepoint(t1)
print(dm.state, dm.delta)
dm.abort(t1)
