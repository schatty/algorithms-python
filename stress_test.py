def stress_test(foo, foo_dumb, arg_generator, n_iter=1e3):
    i = 0
    for i in range(n_iter):
        if i % 1e2 == 0:
            print("Processing: ", i)
        a = arg_generator()
        result_1 = foo_dumb(*a)
        result_2 = foo(*a)
        if result_1 != result_2:
            print("Wrong Result")
            print("Input data: ", a)
            print("Expected: ", result_1)
            print("Got: ", result_2)
            break
    if i == n_iter-1:
        print("OK.")