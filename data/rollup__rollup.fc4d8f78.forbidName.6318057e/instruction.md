# Bug Report

### Describe the bug

I'm experiencing an issue where variable renaming is causing name collisions in the bundled output. It seems like the name collision prevention mechanism isn't working properly - variables that should be forbidden from using certain names are still being renamed to those exact names.

### Reproduction

```js
// Example scenario where this occurs:
// When bundling code with multiple variables that need different names
// to avoid conflicts, the bundler is renaming variables to names that
// should be forbidden

// Input code with potential naming conflicts
const x = 1;
function test() {
  const x = 2; // Should be renamed to avoid collision
  return x;
}

// Expected: inner 'x' renamed to something like 'x$1' or 'x_1'
// Actual: both variables end up with conflicting names in output
```

### Expected behavior

When a variable name is marked as forbidden (to prevent collisions), the bundler should avoid renaming other variables to that name. The `forbidName()` mechanism should properly track and prevent name reuse.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production builds where minified code has variable name conflicts that break functionality. The forbidden names set doesn't seem to be accumulating names correctly.

---
Repository: /testbed
