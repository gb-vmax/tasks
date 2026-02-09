# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX content. When using backticks for inline code, the closing backticks are being consumed incorrectly, causing the code text to not be properly delimited.

### Reproduction

```mdx
This is some text with `inline code` in it.
```

When parsing this, the inline code block doesn't close properly. The backtick sequence matching seems to be off - it's checking if the size matches the opening sequence at the wrong point in the logic.

### Expected behavior

Inline code blocks should be properly closed when the matching number of backticks is encountered. For example:
- `` `code` `` should parse as inline code with content "code"
- ``` ``code`` ``` should parse as inline code with content "code"
- The closing sequence should match the opening sequence length

### Additional context

This appears to be related to the `sequenceClose` function in the code text tokenizer. The sequence matching logic seems to have been reordered in a way that causes the size check to happen before consuming the backtick character, which breaks the proper matching behavior.

---
Repository: /testbed
