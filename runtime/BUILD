py_library(
    name = "runtime",
    srcs = ["functions.py"],
)

py_binary(
    name = "run",
    srcs = ["run.py"],
    deps = [":runtime"],
)

py_test(
    name = "test_functions",
    srcs = ["test_functions.py"],
    deps = [":runtime"],
)

py_test(
    name = "test_run",
    srcs = ["test_run.py"],
    deps = [":runtime"],
)
