# Bug Report

### Describe the bug

When using watch hooks with rollup, the output from hook commands is being sent to stdout instead of stderr. This causes issues when trying to capture the actual build output separately from hook execution logs.

### Reproduction

Set up a rollup watch configuration with a custom hook:

```js
// rollup.config.js
export default {
  // ... other config
  watch: {
    onStart: 'echo "Starting build"',
    onBundleEnd: 'echo "Bundle complete"'
  }
}
```

Run rollup in watch mode and try to redirect the build output:

```bash
rollup -c -w > build-output.txt
```

### Expected behavior

The hook command output (like "Starting build", "Bundle complete") should be written to stderr so it doesn't interfere with the actual build output being captured. This way, users can cleanly separate diagnostic/hook messages from the actual bundle output when redirecting streams.

### Current behavior

The hook command output is being written to stdout, which gets mixed with the build output and makes it impossible to cleanly capture just the bundle results.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
