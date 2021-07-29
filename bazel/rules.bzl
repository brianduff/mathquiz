load("@bazel_skylib//lib:paths.bzl", "paths")

def _mq_chapter_impl(ctx):
    srcs = ctx.files.srcs

    outs = []
    for src in srcs:
        out_path = paths.replace_extension(src.basename, ".html")
        # out_map[src] = out_file

        tmp_path = paths.replace_extension(src.basename, ".tmp.md")
        # tmp_map[src] = tmp_file

        out_file = ctx.actions.declare_file(out_path)
        outs.append(out_file)
        tmp_file = ctx.actions.declare_file(tmp_path)
        # outs.append(tmp_file)

        args = [src.path, tmp_file.path]

        ctx.actions.run(
            inputs = [src],
            outputs = [tmp_file],
            tools = [ctx.executable.run_generator],
            progress_message = "Generating executed markdown %s" % tmp_file.short_path,
            executable = ctx.executable.run_generator,
            arguments = args,
        )

        # Invoke pandoc on each file.
        #    args = ctx.actions.args()
        ctx.actions.run_shell(
            inputs = [tmp_file],
            command = "pandoc --shift-heading-level-by=-1 --from=markdown --standalone --mathjax -t html " + tmp_file.path + " -o " + out_file.path,
            outputs = [out_file],
        )

    return [DefaultInfo(files = depset(outs))]

mq_chapter = rule(
    implementation = _mq_chapter_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = [".md"]),
        "run_generator": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
            default = Label("//runtime:run_generator"),
        ),
    },
)
