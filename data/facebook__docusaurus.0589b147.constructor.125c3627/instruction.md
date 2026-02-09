# Bug Report

### Describe the bug

I'm experiencing an issue with property and attribute handling in MDX. After a recent update, it seems like properties and attributes are being treated as objects instead of strings, which is breaking my component rendering.

When I try to access element properties or attributes, I'm getting an object with a `value` key instead of the actual string value I expect. This is causing unexpected behavior in my MDX components.

### Reproduction

```js
// When creating an element with properties
const info = new Info('className', 'class');

// Expected: info.property === 'className'
// Actual: info.property === { value: 'className' }

// Also, attribute seems to reference the same object as property
console.log(info.attribute === info.property); // true (should be false)
```

### Expected behavior

- `info.property` should be a string value, not an object
- `info.attribute` should be its own string value, not a reference to the property object
- Properties and attributes should be independent values

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking my existing MDX setup where I rely on these being simple string values. Any help would be appreciated!

---
Repository: /testbed
