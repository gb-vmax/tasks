# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where it's not correctly identifying valid break points in the content. It seems like the logic for determining when a break is allowed has been inverted somehow.

### Reproduction

When parsing MDX content with certain constructs that have `previous` conditions, the parser is now accepting breaks in places where it shouldn't and rejecting them where they should be valid. 

For example:

```mdx
Some text with special characters or constructs that should allow breaks
```

The parser now incorrectly evaluates the break conditions - it returns `true` when the `previous` condition check fails (when it should return `false`), and vice versa.

### Expected behavior

The parser should correctly identify valid break points based on the construct's `previous` condition. When a construct has a `previous` check that returns `false`, that should indicate the break is NOT valid at that position.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing parsing errors in content that was previously working fine. The break detection logic seems to have the condition backwards.

---
Repository: /testbed
