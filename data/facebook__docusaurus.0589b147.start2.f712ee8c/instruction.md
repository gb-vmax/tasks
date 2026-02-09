# Bug Report

### Describe the bug

After a recent update, inline code blocks in MDX files are not being parsed correctly. The markdown processor seems to be entering token states in the wrong order, causing code text sequences to not be properly recognized.

### Reproduction

```mdx
This is a paragraph with `inline code` in it.
```

When processing this MDX content, the inline code (text between backticks) is not being tokenized properly. The parser appears to be confused about the order of entering the codeText and codeTextSequence states.

### Expected behavior

Inline code blocks wrapped in backticks should be correctly parsed and rendered as code elements. The tokenizer should properly handle the sequence of entering codeText tokens.

### Additional context

This appears to affect any MDX file that uses inline code syntax with single backticks. The issue seems to be in the tokenization phase where the parser enters different states for code text processing.

---
Repository: /testbed
