# Bug Report

### Describe the bug

When a plugin's `renderChunk` hook throws an error, the build process silently continues without any warning or error message. The error gets caught and swallowed, making it extremely difficult to debug issues in custom plugins.

### Reproduction

```js
// In a custom rollup plugin
export default {
  name: 'my-plugin',
  renderChunk(code, chunk) {
    // This error will be silently ignored
    throw new Error('Something went wrong in renderChunk');
  }
}
```

### Expected behavior

When a plugin's `renderChunk` hook throws an error, the build should fail with a clear error message indicating which plugin caused the issue. Silent failures make debugging nearly impossible.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
