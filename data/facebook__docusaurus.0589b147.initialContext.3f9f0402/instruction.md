# Bug Report

### Describe the bug

I'm experiencing an issue where the parser's context stack appears to be shared across multiple parser instances, causing unexpected behavior when parsing multiple files or running the parser concurrently.

### Reproduction

```js
const parser1 = new Parser();
const parser2 = new Parser();

// Both parsers seem to share the same initial context
const ctx1 = parser1.initialContext();
const ctx2 = parser2.initialContext();

// Modifying one affects the other
ctx1.push(someNewContext);

// ctx2 is also affected, which shouldn't happen
```

When parsing multiple MDX files in parallel or creating multiple parser instances, the context state seems to leak between instances. This causes parsing errors or incorrect AST generation, especially when processing files simultaneously.

### Expected behavior

Each parser instance should maintain its own independent context stack. Modifications to one parser's context should not affect other parser instances.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
