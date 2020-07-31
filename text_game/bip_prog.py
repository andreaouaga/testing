import time


def bip(total):
    print("执行开始".center(total//2, '-'))
    start = time.perf_counter()
    try:
        for i in range(0, total):
            a = '*' * i
            b = '.' * (total - i)
            c = (i / total) * 100
            print('\a')
            time.sleep(7)
            dur = time.perf_counter() - start
            print("\r{:.^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur), end='')
        print('\a'*2)
        print('\n'+"执行结束".center(total//2, '-'))
    finally:
        return i
        


def write_a_record(total):
    timestr = time.strftime('%Y-%m-%d  %H:%M:%S', time.gmtime())
    record = timestr + f'完成{total}个单词\n'
    with open('record.txt', 'a', encoding='utf8') as file:
        file.write(record)        
       

if __name__ == "__main__":
    total = 100
    a = bip(total)
    write_a_record(a + 1)
