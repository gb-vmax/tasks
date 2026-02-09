# Bug Report

### Describe the bug

I'm encountering an issue where variables with empty string global names are not being rendered correctly. When a variable has `globalName` set to an empty string (`''`), it seems to be falling through to use the original name instead of respecting the empty string value.

### Reproduction

```js
const variable = new Variable({
  name: 'myVar',
  globalName: ''
});

// When rendering, expected to get empty string but getting 'myVar' instead
const rendered = variable.getName(getPropertyAccess, useOriginalName);
console.log(rendered); // Outputs: 'myVar' (incorrect)
// Expected: '' (empty string)
```

### Expected behavior

When `globalName` is explicitly set to an empty string, the `getName()` method should return that empty string rather than falling back to the original variable name. Empty strings are valid global names and should be treated differently from `undefined` or `null`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
