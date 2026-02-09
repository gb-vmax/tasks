# Bug Report

### Describe the bug

I'm experiencing an issue with the `toString()` method on VFile objects. When I try to convert a VFile to a string, it's returning an empty string instead of the actual file content.

### Reproduction

```js
const vfile = new VFile({ value: 'Hello, world!' });

// This returns an empty string instead of 'Hello, world!'
console.log(vfile.toString());
```

Also noticed that when the value is explicitly set to `null`, it doesn't behave as expected:

```js
const emptyFile = new VFile({ value: null });
// Expected: empty string
// Actual: throws error or unexpected behavior
console.log(emptyFile.toString());
```

### Expected behavior

- When a VFile has a string value, `toString()` should return that string value
- When a VFile has `null` or `undefined` value, `toString()` should return an empty string
- When a VFile has a buffer value, it should decode it properly

### System Info

- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently - was working fine before. Any help would be appreciated!

---
Repository: /testbed
