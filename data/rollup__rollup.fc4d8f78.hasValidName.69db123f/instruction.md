# Bug Report

### Describe the bug

I'm encountering an issue with file emission validation. When trying to emit files with valid names, the validation is incorrectly rejecting them. It seems like the name validation logic is behaving opposite to what it should be.

### Reproduction

```js
// Trying to emit a file with a valid fileName
this.emitFile({
  type: 'asset',
  fileName: 'output.js',
  source: 'console.log("test");'
})

// This should work but is being rejected as invalid
```

Also noticed that when providing both `fileName` and `name` properties, the validation behavior is unexpected. It seems to require both properties to be present when it should accept either one.

### Expected behavior

Files with valid names (non-path-fragment strings) should pass validation. The emitter should accept files when either `fileName` OR `name` is provided with a valid value, not require both to be present.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
