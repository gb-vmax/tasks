# Bug Report

### Describe the bug
Inline code rendering is broken after recent changes. Code enclosed in backticks is not being parsed correctly - either the backticks themselves are showing up in the output or the code blocks are not being recognized at all.

### Reproduction
```markdown
This is some text with `inline code` in it.
```

When parsing the above markdown:
- The inline code is not properly detected
- Backtick sequences seem to be counted incorrectly
- Spacing around code blocks behaves unexpectedly

### Expected behavior
Inline code wrapped in single backticks should be properly tokenized and rendered. The backticks should be consumed correctly and the text between them should be treated as code.

For example:
- `code` should render as inline code
- Multiple backticks like `` `backtick` `` should work for escaping
- Spaces adjacent to backticks should be handled appropriately

### Additional context
This appears to affect the markdown tokenizer's handling of code text sequences. The issue manifests when processing any markdown content that contains inline code blocks.

---
Repository: /testbed
