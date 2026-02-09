# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain GFM (GitHub Flavored Markdown) features are not being processed correctly. It seems like some constructs are being skipped during the parsing phase.

### Reproduction

When parsing markdown with multiple GFM features (like tables, strikethrough, task lists), some of these features are not being resolved properly. For example:

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

~~strikethrough text~~

- [ ] Task item
```

The first construct type gets processed, but subsequent ones of the same type are ignored.

### Expected behavior

All GFM constructs should be properly resolved and rendered in the output, regardless of how many times they appear in the document.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
