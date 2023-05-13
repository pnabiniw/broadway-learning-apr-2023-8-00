from day15.decorators import decorate_me, to_upper, \
    exec_time, login_required
#
#
# @to_upper
# def message():
#     return "Hello World"
#
# # message = decorate_me(message)
# print(message())
#
#
# @to_upper
# def next_message():
#     return "python is awesome"
#
#
# print(next_message())
# import time
#
# start = time.time()
# for i in range(100000000):
#     pass
# end = time.time()
# execution_time = end - start
# print(execution_time)
#
#
# @exec_time
# def test_fxn():
#     for i in range(100000000):
#         pass
#     return "Done !!"
#
#
# print(test_fxn())


@login_required
def get_message():
    return "Learning at broadway !"


print(get_message())
