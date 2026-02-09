# Bug Report

### Describe the bug
After a recent update, ATX-style headings in MDX files are not being parsed correctly. The headings appear to be completely broken and not rendering at all in the output.

### Reproduction
```mdx
# Heading 1
## Heading 2
### Heading 3
```

When processing the above MDX content, the headings are not recognized or parsed. It seems like the tokenizer is failing to properly enter the heading context.

### Expected behavior
ATX headings (using `#` syntax) should be properly tokenized and rendered as heading elements in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have broken after a recent change to the heading tokenizer. The headings were working fine in the previous version.

---
Repository: /testbed
