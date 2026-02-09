# Bug Report

### Describe the bug

I'm experiencing an issue with VFile initialization where custom properties passed in the options object are not being properly set on the VFile instance. When I create a VFile with additional properties beyond the standard ones, those properties don't appear on the resulting object.

### Reproduction

```js
const file = new VFile({
  value: 'some content',
  path: '/path/to/file.md',
  customProp: 'custom value',
  metadata: { foo: 'bar' }
});

console.log(file.customProp); // undefined
console.log(file.metadata); // undefined
```

### Expected behavior

Custom properties that aren't in the standard `order` array should still be copied to the VFile instance. In the example above, `file.customProp` should be `'custom value'` and `file.metadata` should be `{ foo: 'bar' }`.

This used to work in previous versions where I could extend VFile with arbitrary properties for my use case. Now those properties are silently ignored.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
