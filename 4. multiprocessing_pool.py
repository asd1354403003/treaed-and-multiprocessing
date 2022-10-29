# Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2)
    # 自动分配
    res = pool.map(job, range(10))
    print(res)
    # 给一个
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()