This is a simple tool that generates math quizzes with random / variable questions that can be expressed in Python syntax.

The questions directory contains a bunch of example questions. To generate html versions, you need to first install `pandoc`. This can be done on MacOS via:

`brew install pandoc`

After that, you can build the html files via:

`bazel build questions/...`
