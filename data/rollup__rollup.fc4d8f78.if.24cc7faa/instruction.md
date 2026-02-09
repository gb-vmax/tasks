# Bug Report

### Describe the bug
When using watch hooks in CLI mode, the output from hook commands is being redirected to stderr instead of stdout. This causes normal command output to appear in the error stream, which breaks scripts that rely on capturing stdout separately from stderr.

### Reproduction
```bash
# Set up a watch hook that echoes output
rollup -c --watch --watch.onStart="echo 'Starting build...'"
```

The output "Starting build..." appears in stderr instead of stdout, which is unexpected behavior for normal command output.

### Expected behavior
Normal output from watch hook commands should be written to stdout, while only error messages should go to stderr. This allows proper separation of standard output and error streams when piping or redirecting output.

### Additional context
This affects any scripts or CI/CD pipelines that capture stdout and stderr separately. Previously, command output was correctly sent to stdout, but now everything goes to stderr which makes it difficult to distinguish between normal output and actual errors.

---
Repository: /testbed
