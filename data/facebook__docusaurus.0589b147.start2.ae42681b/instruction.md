# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where the `marker` variable in the `tokenizeAttention` function is being cleared prematurely. This causes problems when processing attention sequences (bold/italic markdown syntax) because the marker tracking gets reset before the sequence is fully processed.

### Reproduction

```markdown
**bold text**
*italic text*
```

When parsing the above markdown with MDX, the attention sequence tokenization doesn't work correctly. The marker that tracks whether we're processing `*` or `_` gets set to `undefined` before the `inside` function can properly consume the characters.

### Expected behavior

The parser should correctly tokenize attention sequences by maintaining the marker value throughout the entire tokenization process. The marker should only be cleared after the sequence has been fully consumed, not before `effects.enter("attentionSequence")` is called.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as the tokenization was working correctly before. The issue seems related to the order of operations in the `start2` function where the marker is being cleared too early in the process.

---
Repository: /testbed
