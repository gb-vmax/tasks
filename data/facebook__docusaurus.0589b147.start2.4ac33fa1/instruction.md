# Bug Report

### Describe the bug

After a recent update, emphasis markers (asterisks and underscores) in MDX content are not being parsed correctly. The tokenization logic appears to be broken, causing emphasis syntax like `*text*` or `_text_` to either not render as emphasized text or produce unexpected output.

### Reproduction

```mdx
# Test Document

This should be *emphasized* text.

This should be **bold** text.

This should be _also emphasized_ text.
```

When processing the above MDX content, the emphasis markers are not being recognized properly. The text remains unformatted or the parser throws an error during tokenization.

### Expected behavior

The emphasis markers should be correctly tokenized and the text should render with appropriate formatting:
- `*text*` should render as emphasized/italic
- `**text**` should render as bold
- `_text_` should render as emphasized/italic

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
