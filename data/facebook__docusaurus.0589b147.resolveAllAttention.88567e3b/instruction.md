# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/strong emphasis parsing in MDX content. When using single asterisks or underscores for emphasis (italic) and double asterisks/underscores for strong emphasis (bold), the markdown isn't being processed correctly.

### Reproduction

```mdx
This should be *italic* text.
This should be **bold** text.
This should be ***bold and italic*** text.
```

When rendering this MDX content, the emphasis markers are not being properly converted to their HTML equivalents (`<em>` and `<strong>` tags). The text either remains as plain text with the asterisks visible, or the formatting is applied incorrectly.

### Expected behavior

- Single asterisks/underscores should produce italic text (`<em>`)
- Double asterisks/underscores should produce bold text (`<strong>`)
- Triple asterisks/underscores should produce bold+italic text (`<strong><em>`)

The attention sequences should be properly matched and converted to the appropriate HTML tags.

### Additional context

This seems to affect the parsing logic for attention sequences (emphasis markers). The issue appears when processing markdown emphasis syntax within MDX documents.

---
Repository: /testbed
