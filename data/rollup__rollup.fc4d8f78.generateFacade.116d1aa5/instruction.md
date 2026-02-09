# Bug Report

### Describe the bug

After a recent update, the build process is failing with a syntax error. It looks like there's an incomplete statement in the chunk generation code that's causing the build to break.

### Reproduction

Try to build any project with the latest version and you'll get a syntax error during the build process. The error occurs when generating facade chunks.

```js
// Any basic rollup config should trigger this
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}
```

### Expected behavior

The build should complete successfully without syntax errors.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have broken in the most recent commit. The code won't even parse properly now.

---
Repository: /testbed
