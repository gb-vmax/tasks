# Bug Report

### Describe the bug

I'm encountering an issue with emphasis/strong emphasis parsing in markdown content. When using multiple asterisks or underscores for emphasis markers, the parser seems to be skipping or incorrectly matching opening and closing sequences.

### Reproduction

```js
// Example markdown that demonstrates the issue:
const markdown = `**bold** text *italic*`;

// When parsing, the emphasis sequences don't match correctly
// The opening marker at index 0 is being skipped during the backward search
```

The problem appears when the parser is trying to resolve attention sequences (emphasis/strong emphasis markers). The backward iteration through events seems to start from the wrong position, causing the first potential opening marker to be missed.

### Expected behavior

All emphasis markers should be properly matched with their corresponding opening/closing pairs. The parser should check all possible opening sequences when looking for matches, including the one at index 0.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

This seems like it could be related to how the loop counter is being decremented when searching backwards through the events array. Would appreciate if someone could take a look at the `resolveAllAttention` function.

---
Repository: /testbed
