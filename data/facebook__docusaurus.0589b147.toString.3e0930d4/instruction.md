# Bug Report

### Describe the bug

The `toString()` method in VFile is returning incorrect values when dealing with non-string content. When the value is a Buffer or Uint8Array, it's being returned directly instead of being decoded to a string.

### Reproduction

```js
const file = new VFile();
file.value = Buffer.from('Hello World');

// This returns the Buffer object itself instead of 'Hello World'
console.log(file.toString());
// Expected: 'Hello World'
// Actual: Buffer object
```

Also, when the value is `undefined`, it's not being handled properly:

```js
const file = new VFile();
// value is undefined by default

console.log(file.toString());
// Should return empty string but behavior is inconsistent
```

### Expected behavior

- When `value` is a Buffer/Uint8Array, `toString()` should decode it and return the string representation
- When `value` is `undefined`, it should return an empty string
- When `value` is already a string, it should return that string as-is

### System Info
- Using the remark@15.0.1 vendor bundle
- Node version: 18.x

---
Repository: /testbed
