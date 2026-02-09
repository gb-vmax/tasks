# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where it's rejecting valid function-based parsers. After a recent update, when I try to use a custom parser function, I get a TypeError saying it needs an object instead.

### Reproduction

```js
const unified = require('unified');
const myParser = function() {
  // custom parser implementation
  return {
    parse: function(doc) {
      // parsing logic
    }
  };
};

const processor = unified().use(function() {
  this.Parser = myParser;
});

// This now throws: TypeError: Cannot `parse` without `value`
processor.parse('# Hello');
```

### Expected behavior

The processor should accept function-based parsers like it did before. Functions are valid parser implementations and should not be rejected.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
