# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX. When using backticks for inline code, the parser seems to be treating non-backtick characters incorrectly, causing unexpected behavior in code text tokenization.

### Reproduction

```markdown
This is `inline code` in MDX.
```

When parsing this markdown, the inline code block doesn't get recognized properly. The backticks and content between them should be tokenized as code text, but instead the parser appears to be entering the wrong state for regular characters.

### Expected behavior

The content between backticks should be properly recognized and tokenized as inline code. The parser should:
1. Detect the opening backtick sequence
2. Process the content between backticks as code text data
3. Detect the closing backtick sequence and exit properly

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The tokenizer logic for handling characters between backticks doesn't seem to be working as expected.

---
Repository: /testbed
