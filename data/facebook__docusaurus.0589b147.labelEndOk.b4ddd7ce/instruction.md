# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links with certain edge cases are causing unexpected behavior. It seems like the parser is not handling cases where the code point might be null or undefined properly, which leads to incorrect parsing results or potential crashes.

### Reproduction

```js
// Parsing markdown with links that have edge cases
const markdown = `[link text](url)`;
const result = remark().parse(markdown);

// In certain scenarios with malformed or edge-case markdown,
// the parser doesn't handle null/undefined code points correctly
```

I've noticed this happens particularly when:
1. Processing markdown with unusual link structures
2. Working with input that has incomplete or malformed link syntax
3. Edge cases where the tokenizer encounters unexpected end-of-input

### Expected behavior

The parser should gracefully handle all code point values including null and undefined without breaking or producing incorrect AST output. Links should be parsed consistently regardless of edge cases in the input.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

This seems to be related to how the label end tokenizer processes code points. Would appreciate any guidance on this!

---
Repository: /testbed
