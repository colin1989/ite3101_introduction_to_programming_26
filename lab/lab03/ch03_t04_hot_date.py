from datetime import datetime

now = datetime.now()
print('%02d-%02d-%02d' % (now.month, now.date, now.year))