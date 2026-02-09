# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX not being parsed correctly. The parser seems to be returning unexpected values when processing the opening sequence of code fences (triple backticks or tildes).

### Reproduction

```mdx
```javascript
const example = 'test';
```
```

When this MDX content is parsed, the tokenizer for fenced code blocks appears to be returning the wrong value from the `start2` function, which is causing the parser to fail or behave unexpectedly.

### Expected behavior

Fenced code blocks should be properly tokenized and parsed. The opening sequence should be correctly identified and the parser should continue processing the rest of the code block content.

### Additional context

This seems related to how the tokenizer state machine handles the initial code point when starting to parse a fenced code block. The function is supposed to delegate to `beforeSequenceOpen` but something appears wrong with the return value flow.

---
Repository: /testbed
