# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when parsing ATX headings (headings with `#` symbols) in markdown. The parser seems to get stuck in an infinite loop and eventually crashes with a stack overflow error.

### Reproduction

```js
const markdown = `# Heading with text`;

// Parser hangs and crashes with stack overflow
const result = remark.parse(markdown);
```

This happens specifically when parsing headings that contain text content after the `#` symbols. Simple headings without text seem to work fine.

### Expected behavior

The parser should successfully parse ATX headings with text content and return the appropriate AST without crashing.

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to have started recently, possibly after a recent update. Any help would be appreciated!

---
Repository: /testbed
