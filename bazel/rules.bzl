load("@bazel_skylib//lib:paths.bzl", "paths")

def _mq_chapter_impl(ctx):
  srcs = ctx.files.srcs

  outs = []
  out_map = {}
  tmp_map = {}
  for src in srcs:
    out_path = paths.replace_extension(src.basename, ".html")
    # out_map[src] = out_file

    tmp_file = paths.replace_extension(src.basename, ".tmp.md")
    # tmp_map[src] = tmp_file

    out_file = ctx.actions.declare_file(out_path)

    # Invoke pandoc on each file.
    args = ctx.actions.args()
    ctx.actions.run_shell(
      command = "pandoc",
      outputs = [out_file]
    )


mq_chapter = rule(
  implementation = _mq_chapter_impl,
  attrs = {
    "srcs": attr.label_list(allow_files=[".md"])
  }
)
