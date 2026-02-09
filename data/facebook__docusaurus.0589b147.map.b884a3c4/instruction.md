# Bug Report

### Describe the bug

I'm experiencing an issue with object merging in the remark parser. When trying to merge objects, the behavior seems incorrect - objects that should be merged are not being combined properly.

### Reproduction

```js
const left = { foo: 'bar' };
const right = { baz: 'qux' };

// Expected: left should be { foo: 'bar', baz: 'qux' }
// Actual: left remains { foo: 'bar' }
map(left, right);
console.log(left); // { foo: 'bar' } - missing the merged properties
```

Also noticed that when `left` is undefined or null, the merge doesn't happen at all even when `right` has properties.

### Expected behavior

The `map` function should merge properties from the `right` object into the `left` object when both are provided. This is standard object merging behavior that was working in previous versions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
