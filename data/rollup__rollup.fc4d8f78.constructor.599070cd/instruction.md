# Bug Report

### Describe the bug

I'm experiencing an issue with the watch mode where files that should be excluded are being watched, and files that should be included are being excluded. It seems like the include/exclude patterns are being applied in reverse.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist'
  },
  watch: {
    include: 'src/**',
    exclude: 'node_modules/**'
  }
}
```

When running in watch mode:
1. Changes to files in `node_modules/` trigger rebuilds (they shouldn't)
2. Changes to files in `src/` are ignored (they should trigger rebuilds)

The watch patterns seem to be inverted - files matching the exclude pattern are being watched, while files matching the include pattern are being ignored.

### Expected behavior

Files matching the `include` pattern should trigger rebuilds, and files matching the `exclude` pattern should be ignored by the watcher.

### Additional context

This is causing my development workflow to break as every change in node_modules triggers unnecessary rebuilds, while actual source file changes are being ignored.

---
Repository: /testbed
