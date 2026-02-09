# Bug Report

### Describe the bug

I'm encountering an issue with the MDX tokenizer where it's skipping the first construct in a list when attempting to parse content. It seems like the tokenizer is starting at index 1 instead of 0, which causes the first available construct to be ignored during parsing.

### Reproduction

When processing MDX content with multiple possible constructs, the first construct in the list is never attempted. For example:

```js
// Given a list of constructs: [constructA, constructB, constructC]
// Only constructB and constructC are tried, constructA is skipped
```

This results in valid MDX syntax not being recognized if it matches the first construct in the list.

### Expected behavior

The tokenizer should iterate through all constructs in the list starting from index 0, attempting each one in order until a match is found. The first construct should not be skipped.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
