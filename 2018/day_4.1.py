import collections
from datetime import datetime
guards = collections.defaultdict(list)
times = collections.defaultdict(int)

#indata_file = open("./2018/test_input_day4.txt", "r")
indata_file = open("./2018/input_day4.txt", "r")
indata_txt = indata_file.read()

for line in sorted(indata_txt.splitlines()):
    time, event = line.split('] ')
    time = datetime.strptime(time[1:], "%Y-%m-%d %H:%M")
    if 'Guard' in event:
        guard = int(event.split()[1][1:])
    elif 'falls' in event:
        start = time
    elif 'wakes' in event:
        end = time
        guards[guard].append((start.minute, end.minute))
        times[guard] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60)], key=lambda i: i[1])

print(guard, minute)
print('Sleepiest guard X minute slept most:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('Sleepy guard X minute most often slept:', guard * minute)
    