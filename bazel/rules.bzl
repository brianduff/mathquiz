load("@bazel_skylib//lib:paths.bzl", "paths")

def _mq_chapter_impl(ctx):
    srcs = ctx.files.srcs

    outs = []
    for src in srcs:
        out_path = paths.replace_extension(src.basename, ".html")

        tmp_path = paths.replace_extension(src.basename, ".tmp.md")

        out_file = ctx.actions.declare_file(out_path)
        outs.append(out_file)
        tmp_file = ctx.actions.declare_file(tmp_path)

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
        ctx.actions.run_shell(
            inputs = [tmp_file],
            command = "pandoc --shift-heading-level-by=-1 --from=markdown --standalone --mathjax -t html " + tmp_file.path + " -o " + out_file.path,
            outputs = [out_file],
        )

    toc_md_file = ctx.actions.declare_file("toc.md")

    ctx.actions.run(
        inputs = ctx.files.srcs,
        outputs = [toc_md_file],
        tools = [ctx.executable.toc_generator],
        executable = ctx.executable.toc_generator,
        arguments = [toc_md_file.path] + [f.path for f in ctx.files.srcs],
    )

    toc_html_file = ctx.actions.declare_file("toc.html")
    outs.append(toc_html_file)
    ctx.actions.run_shell(
        inputs = [toc_md_file],
        command = "pandoc --metadata title='" + ctx.attr.title + "' --from=markdown --standalone -t html " + toc_md_file.path + " -o " + toc_html_file.path,
        outputs = [toc_html_file],
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
        "toc_generator": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
            default = Label("//toc:toc_generator"),
        ),
        "title": attr.string(),
    },
)
