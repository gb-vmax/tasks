# Bug Report

### Describe the bug

I'm experiencing an issue with nested container handling in markdown parsing. When processing documents with nested block-level containers (like nested lists or blockquotes), the parser seems to be exiting one too many containers, causing unexpected behavior in the document structure.

### Reproduction

```js
const markdown = `
> outer quote
> > nested quote
> > still nested
> back to outer
`;

const result = remark().parse(markdown);
// The nesting structure is incorrect - containers are being closed prematurely
```

Another example with nested lists:

```js
const markdown = `
- item 1
  - nested item 1
  - nested item 2
- item 2
`;

const ast = remark().parse(markdown);
// Nested list items appear at wrong depth level
```

### Expected behavior

Nested containers should maintain proper hierarchy. When exiting containers, only the appropriate number of container levels should be closed, preserving the correct nesting structure in the resulting AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The container stack management appears to be off by one somewhere, causing an extra container to be exited when it shouldn't be.

---
Repository: /testbed
