# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX when the code fence doesn't have any info string (language identifier). The parser seems to be handling `null` values incorrectly in the `infoBefore` function, causing unexpected behavior when processing code blocks.

### Reproduction

```mdx
```
some code here
```
```

When parsing the above MDX with a code fence that has no info string (no language specified after the opening backticks), the parser doesn't properly handle the case where `code2` is `null`.

### Expected behavior

The parser should correctly process fenced code blocks regardless of whether they have an info string or not. A code block without a language identifier should still be parsed and rendered properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
