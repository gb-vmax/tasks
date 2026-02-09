# Bug Report

### Describe the bug

I'm experiencing an issue with parsing nested block structures in markdown. When I have indented code blocks or other block-level elements that should continue across multiple lines, the parser seems to be incorrectly determining which lines are lazy continuations.

### Reproduction

```js
const markdown = `
> This is a quote
>     indented code block
>     more code
> continuing quote
`;

const result = remark().parse(markdown);
// The indented code block is not being parsed correctly
// Lines that should be part of the block are being treated as lazy continuations
```

Another example that triggers the issue:

```js
const markdown = `
- List item with:
      code block inside
      more code lines
  continuation of list item
`;

const ast = remark().parse(markdown);
// The code block structure is broken
```

### Expected behavior

The parser should correctly identify non-lazy continuation lines in nested block structures. Lines that are properly indented within block containers (like blockquotes or list items) should be parsed as part of those blocks, not treated as lazy continuations.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
