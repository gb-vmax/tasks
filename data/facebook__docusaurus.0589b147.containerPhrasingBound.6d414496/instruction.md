# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where phrasing content (inline elements) inside container elements are not being processed correctly. The parent-child relationship seems to be inverted, causing the parser to fail when handling nested inline content.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
**Bold text** with [a link](https://example.com) inside.
`;

const result = processor.parse(markdown);
// Parser fails to correctly associate inline elements with their parent container
```

When parsing markdown with inline elements (emphasis, links, etc.) nested within block-level containers, the context binding appears incorrect and the parent-child hierarchy gets mixed up.

### Expected behavior

The parser should correctly handle the parent-child relationship between container elements and their phrasing content. Inline elements should be properly associated with their parent containers during the parsing phase.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
