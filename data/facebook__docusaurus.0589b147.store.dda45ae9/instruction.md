# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer's state restoration seems to be off by one. When the parser needs to backtrack and restore a previous state, it appears to be restoring to an incorrect event index, which causes parsing errors or unexpected behavior in certain edge cases.

### Reproduction

This is tricky to reproduce consistently, but it happens when:

1. The MDX parser encounters a construct that needs to be backtracked
2. The tokenizer stores the current state using `store()`
3. Later, when `restore()` is called, the events array seems to be restored to the wrong position

The issue manifests when parsing complex MDX structures that involve nested components or ambiguous syntax that requires the parser to try multiple interpretations.

Example MDX that triggers the issue:
```mdx
<Component>
  Some content with {expression}
  More nested content
</Component>
```

### Expected behavior

The tokenizer should correctly restore to the exact state before attempting a construct, allowing the parser to try alternative parsing strategies without corruption of the event stream.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
