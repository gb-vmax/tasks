# Bug Report

### Describe the bug

I'm encountering an issue with inline code rendering in markdown. When using backticks for inline code (e.g., `` `code` ``), the output is not being generated correctly. The inline code blocks appear to be missing or showing unexpected behavior.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = 'This is some `inline code` in text';
const result = processor.processSync(markdown);

console.log(result);
// Expected: inline code should be properly parsed as inlineCode type
// Actual: inline code is not rendering as expected
```

### Expected behavior

Inline code blocks wrapped in backticks should be parsed and rendered correctly as inline code elements. The AST node should have type `inlineCode` with the proper value.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
