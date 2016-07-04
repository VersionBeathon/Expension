# _*_ coding:utf-8 _*_
from datetime import datetime
from datetime import timedelta
from datetime import timezone
now = datetime.now()
print(now)
dt = datetime(2015, 4, 4, 4, 4, 44)
print(dt)

# 转换为unix时间戳

print(now.timestamp())

# 将unix时间戳转换为本地时间


t = 1467615839
print(datetime.fromtimestamp(t))

# 将unix时间戳转换为UTC标准时区的时间(格林威治)

print(datetime.utcfromtimestamp(t))

# 格式化时间str->datetime

cday = datetime.strptime('2015,5,5 5,5,5', '%Y,%m,%d %H,%M,%S')
print(cday)

# datetime->str

print(now.strftime('%a-%b-%d,%H:%M'))

# datetime加减

print(now + timedelta(hours=10))
print(now + timedelta(days=100))
print(now + timedelta(hours=12, days=10, seconds=100, minutes=10))

# 本地时间转换为UTC时间

tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(now)
print(dt)
print('\n')

# 时区转换
# 获取UTC时间,并强制设置时区为UTC+0
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(now)
print(utc_dt)
print('\n')
# astimezone()将转换时区为北京时间
bj_time = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(now)
print(bj_time)
print("\n")
# 转换时区为东京时间
dj_time = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(now)
print(dj_time)
print("\n")
# 将北京时间转换为东京时间
tokyo_time = bj_time.astimezone(timezone(timedelta(hours=9)))
print(bj_time)
print(tokyo_time)


def to_timestamo(dt_str):
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc_5 = timezone(timedelta(hours=5))
    time_5 = time.replace(tzinfo=utc_5)
    print(time_5)
    return time_5.timestamp()
print(to_timestamo('2015-1-21 9:01:30'))