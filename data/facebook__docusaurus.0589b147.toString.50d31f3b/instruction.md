# Bug Report

### Describe the bug

When calling `toString()` on VFile objects, the method returns an empty string even when the file has valid content. This appears to affect both string and buffer values stored in the `value` property.

### Reproduction

```js
const file = new VFile({value: 'Hello, world!'});
console.log(file.toString()); // Expected: 'Hello, world!', Actual: ''

const fileWithBuffer = new VFile({value: Buffer.from('Test content')});
console.log(fileWithBuffer.toString()); // Expected: 'Test content', Actual: ''
```

### Expected behavior

The `toString()` method should return the string representation of the file's content:
- If `value` is undefined, return an empty string
- If `value` is a string, return that string
- If `value` is a buffer, decode it and return the resulting string

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
