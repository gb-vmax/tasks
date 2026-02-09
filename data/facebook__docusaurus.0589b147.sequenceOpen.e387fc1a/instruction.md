# Bug Report

### Describe the bug

After a recent update, inline code blocks in MDX files are not being parsed correctly. The tokenizer seems to be processing backtick sequences in the wrong order, causing the code text to not be recognized properly.

### Reproduction

```mdx
This is a paragraph with `inline code` that should work.

Multiple backticks like ``code with ` backtick`` should also work.
```

When processing the above MDX content, the inline code blocks are not being tokenized correctly. The opening backtick sequence is exited before the closing sequence is properly matched.

### Expected behavior

Inline code blocks delimited by backticks should be correctly identified and tokenized. The tokenizer should:
1. Consume all opening backticks
2. Process the content between backticks
3. Match the closing backtick sequence
4. Exit the code text sequence at the appropriate time

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

The issue appears to be in the `sequenceOpen` function within the code text tokenizer, where the exit is being called at an unexpected point in the sequence processing.

---
Repository: /testbed
