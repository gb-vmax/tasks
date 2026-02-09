# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX. When using multiple backticks (like `` `` for inline code), the parser seems to be exiting the code text sequence prematurely, which breaks the tokenization of inline code blocks.

### Reproduction

```mdx
This is some text with ``inline code`` using double backticks.
```

When parsing the above MDX content, the inline code block is not recognized correctly. The parser appears to exit the sequence after consuming each backtick instead of waiting for the complete opening sequence.

### Expected behavior

The parser should consume all consecutive backticks in the opening sequence before moving to the content between the backticks. For example, `` `` should be properly tokenized as a complete inline code block with double-backtick delimiters.

### Additional context

This affects any inline code that uses multiple backticks (commonly used when you need to include a single backtick inside the code, like `` `backtick` ``). The tokenization logic seems to be exiting the sequence too early in the parsing flow.

---
Repository: /testbed
