import art
import time


(hr, minute, sec) = (
    time.localtime().tm_hour,
    time.localtime().tm_min,
    time.localtime().tm_sec,
)
count = 0
while count < 100:
    (hr, minute, sec) = (
        time.localtime().tm_hour,
        time.localtime().tm_min,
        time.localtime().tm_sec,
    )
    str_hr, str_minute, str_sec = str(hr), str(minute), str(sec)
    time_str = ":".join((str_hr, str_minute, str_sec))
    new_art = art.text2art(time_str, font="block", chr_ignore=True)
    print(new_art)
    time.sleep(1)
    count += 1
