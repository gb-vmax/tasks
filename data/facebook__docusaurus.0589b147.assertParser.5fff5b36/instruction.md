# Bug Report

### Describe the bug

I'm encountering an error when trying to use the parser functionality. The system is throwing a `TypeError` saying "Cannot `[operation]` without `parser`" even though I'm providing a valid parser function.

### Reproduction

```js
const processor = unified()
  .use(somePlugin)
  .use(function() {
    this.parser = function(doc) {
      // parser implementation
      return parseDocument(doc);
    };
  });

// Attempting to parse throws an error
processor.parse('# Hello World');
```

The error message indicates that no parser is present, but I've clearly defined one. This is blocking me from processing any markdown content.

### Expected behavior

The processor should accept the parser function and successfully parse the input without throwing a TypeError.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
