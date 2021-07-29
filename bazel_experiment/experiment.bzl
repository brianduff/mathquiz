def _simple_rule(ctx):
    out_file = ctx.actions.declare_file(ctx.attr.name)
    ctx.actions.run(
        outputs = [out_file],
        executable = ctx.executable.run_generator,
        arguments = [out_file.path],
    )

    return [DefaultInfo(files = depset([out_file]))]

simple_rule = rule(
    implementation = _simple_rule,
    attrs = {
        "run_generator": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//runtime:run_generator"),
        ),
    },
)
