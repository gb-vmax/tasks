# Bug Report

### Describe the bug

Watch hooks are not being executed in watch mode. When I configure watch hooks like `onStart`, `onBundleStart`, `onBundleEnd`, etc., they don't run at all during the build process.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  watch: {
    onStart() {
      console.log('Build starting...');
    },
    onBundleEnd() {
      console.log('Bundle complete!');
    }
  }
}
```

Run rollup in watch mode and notice that none of the hook messages appear in the console, even though the build completes successfully.

### Expected behavior

The watch hooks should execute when their corresponding events occur during the watch process. The `onStart` hook should run when the build starts, `onBundleEnd` when a bundle finishes, etc.

### System Info
- rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
