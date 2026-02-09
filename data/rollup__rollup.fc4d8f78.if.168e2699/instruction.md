# Bug Report

### Describe the bug

When using watch hooks in CLI mode, the output from hook commands is being sent to the wrong stream. Command output that should go to stderr is instead being written to stdout, which breaks the expected behavior and can interfere with piping/redirection in shell scripts.

### Reproduction

```js
// rollup.config.js
export default {
  // ... config
  watch: {
    onStart: 'echo "Starting build"',
    onBundleStart: 'echo "Bundling..."'
  }
}
```

Run rollup in watch mode and redirect stderr:
```bash
rollup -c -w 2> errors.log
```

### Expected behavior

The output from watch hook commands should be written to stderr (as indicated by the comment in the code), not stdout. This is important for proper stream handling and allows users to separate hook output from the actual build output.

Currently the hook command output goes to stdout instead of stderr, which means it gets mixed with regular output when you're trying to capture errors separately.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux/macOS

---
Repository: /testbed
