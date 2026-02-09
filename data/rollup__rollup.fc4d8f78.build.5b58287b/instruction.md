# Bug Report

### Describe the bug

When building without specifying an output file or directory, the bundle is being written to disk instead of being output to stdout. This breaks the expected behavior where the build output should be printed to the console when no file/dir is specified.

### Reproduction

```bash
# Build without specifying output file or directory
rollup -c rollup.config.js
```

With a config like:
```js
export default {
  input: 'src/index.js',
  output: {
    format: 'es'
    // no file or dir specified - should output to stdout
  }
}
```

### Expected behavior

The bundled code should be printed to stdout when neither `file` nor `dir` is specified in the output options. Instead, it appears the logic is inverted and the bundle is being written to disk.

### Additional context

This used to work correctly in previous versions. The build output would be sent to stdout, which is useful for piping the output to other tools or for debugging purposes without creating temporary files.

---
Repository: /testbed
