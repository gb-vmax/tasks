# Bug Report

### Describe the bug

I'm experiencing an issue with the rendering logic where objects with `disabled: false` are being skipped during rendering. It seems like objects are only being rendered if they don't have a `disabled` property at all, but objects that explicitly set `disabled: false` should also be rendered.

### Reproduction

```js
const obj1 = {
  name: 'test1',
  disabled: false
};

const obj2 = {
  name: 'test2',
  disabled: true
};

const obj3 = {
  name: 'test3'
};

// obj1 is not being rendered even though disabled is explicitly false
// obj2 is correctly skipped (disabled: true)
// obj3 is correctly rendered (no disabled property)
```

### Expected behavior

Objects with `disabled: false` should be rendered the same way as objects without a `disabled` property. Only objects with `disabled: true` should be skipped during rendering.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
