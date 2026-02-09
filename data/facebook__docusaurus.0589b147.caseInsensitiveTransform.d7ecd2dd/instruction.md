# Bug Report

### Describe the bug
I'm experiencing an issue with HTML attribute handling where case-insensitive attributes are not being processed correctly. When I use attributes with mixed or lowercase names, they don't seem to be matched properly.

### Reproduction
```js
// When setting attributes on elements
const element = {
  type: 'element',
  tagName: 'div',
  properties: {
    className: 'test',
    dataValue: 'example'
  }
}

// Attributes with lowercase names are not being recognized
// Expected: attributes should be case-insensitive
// Actual: only uppercase versions are matched
```

### Expected behavior
HTML attributes should be case-insensitive and work correctly regardless of whether they're written in lowercase, uppercase, or mixed case. For example, `className`, `classname`, and `CLASSNAME` should all be treated the same way.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
