# Bug Report

### Describe the bug

When using watch hooks in CLI mode, the output from hook commands is not being displayed correctly. It seems like the stdout from the executed commands is being lost or redirected improperly.

### Reproduction

Set up a watch hook that outputs to stdout:

```json
{
  "watch": {
    "onStart": "echo 'Build starting...'"
  }
}
```

Run the watch command and observe that the echo output doesn't appear in the console, even though the command is executing successfully.

### Expected behavior

The output from watch hook commands should be visible in the console. When a hook like `onStart` or `onEnd` executes a command that writes to stdout, that output should be displayed to the user.

For example, running `echo 'Build starting...'` as a watch hook should print "Build starting..." to the console.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
