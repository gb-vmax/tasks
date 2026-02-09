# Bug Report

### Describe the bug

I'm experiencing an issue with nested container parsing in remark. When processing markdown with nested flow containers, the parser seems to be using the wrong context reference, which leads to incorrect parsing behavior.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
> This is a blockquote
> 
> With multiple paragraphs
> 
> > And nested blockquotes
`;

const result = processor.parse(markdown);
// The nested structure is not being processed correctly
```

When parsing nested flow containers (like blockquotes within blockquotes, or lists within blockquotes), the context appears to be incorrectly passed during the flow container processing. This causes the nested elements to lose their proper parent-child relationship.

### Expected behavior

Nested flow containers should maintain proper hierarchical relationships and be parsed with the correct parent context. The parser should correctly identify and process nested structures.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
