# Bug Report

### Describe the bug

I'm experiencing an issue with rendering objects that have properties starting with underscores. It seems like the rendering behavior has changed and properties prefixed with `_` are now being handled differently than expected.

### Reproduction

```js
const obj = {
  _privateProperty: 'value1',
  publicProperty: 'value2',
  nested: {
    _privateNested: 'value3'
  }
};

// After rendering, the path tracking seems incorrect for underscore-prefixed properties
const rendered = await render(obj);
```

When I have an object with properties that start with an underscore (like `_privateProperty`), the rendering process doesn't seem to track their paths correctly anymore. Previously, these properties were being processed with proper path information, but now they seem to be processed without the path prefix.

### Expected behavior

Properties starting with underscore should still maintain proper path tracking during the rendering process, just like any other property. The path information is important for nested template resolution and error reporting.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
