# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the first element in a list or sequence of nodes is being skipped. When processing multiple markdown elements, the output is missing the initial item.

### Reproduction

```js
const markdown = `
- First item
- Second item
- Third item
`;

const result = parseMarkdown(markdown);
// Expected: "First item Second item Third item"
// Actual: "Second item Third item" (first item is missing)
```

Another example with multiple paragraphs:

```js
const markdown = `
Paragraph one

Paragraph two

Paragraph three
`;

const result = parseMarkdown(markdown);
// The first paragraph doesn't appear in the output
```

### Expected behavior

All elements should be included in the parsed output, including the first one. The parser should process every item in the sequence without skipping any.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
