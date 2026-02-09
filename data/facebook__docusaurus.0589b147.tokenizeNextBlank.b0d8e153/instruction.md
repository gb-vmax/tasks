# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where blank line handling appears to be broken. After a recent update, the parser seems to be exiting with an incorrect token type when processing blank lines in MDX documents.

### Reproduction

```mdx
# Heading

Some content here

Another paragraph after blank line
```

When parsing MDX documents with blank lines between content blocks, the tokenizer is exiting with `"lineEnding"` instead of `"lineEndingBlank"`. This causes the parser to not properly recognize blank lines, which can lead to incorrect document structure interpretation.

### Expected behavior

The tokenizer should properly exit with `"lineEndingBlank"` when processing blank lines, and the `blankLine` attempt should return its result to maintain proper control flow in the parsing logic.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
