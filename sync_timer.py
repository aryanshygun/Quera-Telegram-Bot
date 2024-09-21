import asyncio
import time

def cooking():
    print('cooking started')
    time.sleep(2)
    print('cooking finished')


def boiling():
    print('boiling started')
    time.sleep(4)
    print('boiling finished')



def main():
    start_time = time.time()

    cooking()
    boiling()

    end_time = time.time()

    elapsed = end_time - start_time
    timer = 'elapsed time is ', elapsed
    print(timer)

if __name__ == '__main__':
    main()