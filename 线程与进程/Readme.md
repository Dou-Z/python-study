## python多进程用于什么情况下？
用python写一个CPU密集计算的例子，并比较单线程运行，多线程运行和多进程运行的所用时长

根据multi_thread_process.py的运行结果可以看到，多线程运行比单线程运行更慢，这是因为Python的全局解释器锁（GIL）限制了多线程并行计算的能力。而多进程运行则可以充分利用多核CPU的计算能力，所用时长大大缩短，效率更高。


## multi_thread_process.py多进程代码中存在错误，AttributeError: Can't pickle local object 'multi_process_square_sum.<locals>.<lambda>'，如何修改？
这个错误是由于Python的pickle模块不能序列化lambda函数导致的。解决方法是使用一个普通的函数代替lambda函数。
这里将lambda函数改为了一个名为calc_sum的普通函数，并在调用multiprocessing.Process时传入了该函数的参数。
这个修改后的代码应该可以正常运行，且不会出现pickle错误。

‘已在源文件中修改’

## multi_thread_process.py代码单线程，多线程，多进程的结果都不同是什么原因？怎么修改？

这个结果不同的原因是因为在并行计算的情况下，不同的线程或进程可能以不同的顺序完成计算，因此总时间可能会因此而有所不同。此外，多线程和多进程的运行速度也可能会受到计算机硬件和操作系统的影响。
为了让结果更加稳定，可以进行多次测试并取平均值。另外，为了消除计算顺序的影响，可以对结果进行排序后再进行比较。
修改后的代码在multi_thread_process_改进版.py中

### multi_thread_process_改进版.py进行了10次测试，并对结果进行了排序，以消除计算顺序的影响。同时，对于每个测试，计算了平均运行时间，以得到更稳定的结果

