# Bug Report

### Describe the bug

Optional chaining expressions are being incorrectly tree-shaken when they shouldn't be. Code that has side effects is being removed from the bundle even though it should be preserved.

### Reproduction

```js
// Input code
const obj = getSomeObject();
obj?.method();  // This call has side effects but gets removed

// Another example
data?.items?.forEach(item => {
  console.log(item);  // This code gets removed incorrectly
});
```

When bundling code with optional chaining that has side effects, the bundler is removing these expressions entirely. This appears to happen when the object being accessed could potentially be null/undefined.

### Expected behavior

Optional chaining expressions should only be tree-shaken if they genuinely have no side effects. If the property access or method call could have side effects, it should be preserved in the output bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
