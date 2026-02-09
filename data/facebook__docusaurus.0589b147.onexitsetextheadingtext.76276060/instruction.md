# Bug Report

### Describe the bug

I'm experiencing an issue with setext headings in markdown parsing where the parser crashes with an error when processing certain heading formats. It seems like there's a problem with how the heading text is being handled internally.

### Reproduction

```js
const remark = require('remark');

const markdown = `
Heading Text
============
`;

// Parser crashes here
const result = remark().parse(markdown);
```

When trying to parse markdown with setext-style headings (underlined with `=` or `-`), the parser throws an error about accessing properties on undefined.

### Expected behavior

The parser should successfully parse setext headings without crashing. The markdown should be converted to an AST with proper heading nodes.

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to be a regression as it was working in previous versions. The issue specifically occurs with the setext heading format (underlined headings) but not with ATX headings (using `#` symbols).

---
Repository: /testbed
