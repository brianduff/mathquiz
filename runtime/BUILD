py_library(
    name = "runtime",
    srcs = ["functions.py"],
)

py_binary(
    name = "run_generator",
    srcs = ["run.py"],
    data = [
        "data/continent_area.txt",
        "data/event.txt",
        "data/female.txt",
        "data/fruit.txt",
        "data/male.txt",
        "data/skill.txt",
        "data/sport.txt",
    ],
    main = "run.py",
    visibility = ["//visibility:public"],
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
