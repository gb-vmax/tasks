# Bug Report

### Describe the bug

I'm experiencing an issue where function property access is not being handled correctly during tree-shaking. When accessing properties on functions (like `.length`, `.name`, or custom properties), the bundler is incorrectly treating these accesses as if they were function calls, causing them to be included in the bundle even when they shouldn't be.

### Reproduction

```js
// Example code that triggers the issue
function myFunction() {
  console.log('test');
}

// Accessing function properties
const len = myFunction.length;
const name = myFunction.name;

// These property accesses are being treated incorrectly
// and causing unexpected side effects in the bundled output
```

### Expected behavior

Property access on functions (non-call interactions) should be handled separately from function calls. The tree-shaker should correctly distinguish between:
- `myFunction()` - calling the function
- `myFunction.length` - accessing a property

Currently, it appears that property accesses are being processed through the same code path as function calls, which leads to incorrect side effect analysis.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundler is now treating all interactions with functions as potential calls, even simple property reads.

---
Repository: /testbed
