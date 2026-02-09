# Bug Report

### Describe the bug

Template literals are being incorrectly tree-shaken when accessing their properties or methods. Code that should be retained is being removed during the build process, causing runtime errors.

### Reproduction

```js
const str = `hello ${world}`;
const result = str.toLowerCase();
// result is undefined or causes an error after bundling
```

Another case:
```js
const template = `test ${value}`;
const length = template.length;
// length property access is removed during tree-shaking
```

### Expected behavior

Template literal property accesses and method calls should be preserved during bundling. The code should work the same way after bundling as it does before.

### Additional context

This seems to affect any property access or method call on template literals. Regular string literals work fine, but template literals specifically are being treated incorrectly during the optimization phase.

---
Repository: /testbed
