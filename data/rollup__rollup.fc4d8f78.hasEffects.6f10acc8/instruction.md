# Bug Report

### Describe the bug

I'm experiencing an issue where meta properties like `import.meta` are being treated as having side effects when they shouldn't. This is causing unnecessary code to be included in the bundle even when tree-shaking should remove it.

### Reproduction

```js
// This code should be tree-shaken away since import.meta access has no side effects
if (false) {
  console.log(import.meta.url);
}

// The dead code is not being removed from the bundle
```

Another example:

```js
function unused() {
  const metaUrl = import.meta.url;
  return metaUrl;
}

// This function is never called but still appears in the output
```

### Expected behavior

Code that only accesses `import.meta` properties should be tree-shakeable when it's in dead code branches or unused functions. Meta property access should not be considered as having side effects since it's just reading metadata.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
