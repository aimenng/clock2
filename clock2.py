import time

def focus_timer(minutes):
    seconds = minutes * 60

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f'Time remaining: {timer}', end='\r')
        time.sleep(1)
        seconds -= 1

    print('\nTime\'s up! Take a break.')

if __name__ == '__main__':
    focus_minutes = int(input('请输入专注的分钟数: '))
    focus_timer(focus_minutes)
