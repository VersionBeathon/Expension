import arrow

utc = arrow.utcnow()
print(utc)

utc = utc.replace(hours=-1)
print(utc)

local = utc.to('US/Pacific')
print(local)

print(local.timestamp)

print(local.format('YYYY-MM-DD HH:mm:ss ZZ'))

print(local.humanize())

print(local.humanize(locale='ko_kr'))