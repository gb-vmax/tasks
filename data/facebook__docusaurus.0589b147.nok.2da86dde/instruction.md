# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are being skipped or processed incorrectly. It seems like the parser is not properly iterating through all available constructs when attempting to tokenize content.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test heading

Some paragraph text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = remark().parse(markdown);
console.log(result);
```

When parsing markdown with multiple constructs (headings, paragraphs, lists, etc.), some elements are not being recognized correctly. The parser seems to skip over certain valid constructs that should be matched.

### Expected behavior

The parser should correctly identify and process all markdown constructs in the input. Each construct type (headings, lists, emphasis, etc.) should be properly tokenized and included in the AST.

### Additional context

This appears to be related to how the tokenizer handles construct matching. When one construct fails to match, it should move on to try the next available construct, but something seems off with the iteration logic.

---
Repository: /testbed
