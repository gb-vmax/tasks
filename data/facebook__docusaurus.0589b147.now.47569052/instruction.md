# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in the markdown parser. When parsing entities, the offset calculation seems to be incorrect, causing position information to always report offset as 0 regardless of the actual position in the document.

### Reproduction

```js
const parseEntities = require('./remark-directive');

const input = 'Some text with &amp; entity';
const result = parseEntities(input, {
  position: true,
  warning: (reason, position) => {
    console.log('Position:', position);
    // Expected: position.offset should reflect actual character position
    // Actual: position.offset is always 0
  }
});
```

When parsing text with entities, the position offset is always calculated as 0 instead of the actual character offset in the source. This breaks any tooling that relies on accurate position information for error reporting or source mapping.

### Expected behavior

The `now()` function should return the correct offset value based on the current parsing position. The offset should increment as the parser moves through the document, not stay at 0.

### System Info

- Node version: 18.x
- Package: remark-directive@3.0.0

---
Repository: /testbed
