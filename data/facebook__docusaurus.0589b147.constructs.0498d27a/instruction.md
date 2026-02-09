# Bug Report

### Describe the bug

I'm experiencing issues with parsing GitHub Flavored Markdown (GFM) syntax extensions. It seems like certain markdown constructs are not being recognized or processed correctly, particularly when multiple syntax extensions are being combined.

### Reproduction

```js
// Using remark-gfm to parse markdown with multiple extensions
import remarkGfm from 'remark-gfm'

const markdown = `
# Test Document

Some text with autolinks and other GFM features.

https://example.com

- [ ] Task item
- [x] Completed task
`

// Parse the markdown
const result = parseMarkdown(markdown)

// Expected: All GFM features should be recognized
// Actual: Some syntax extensions are missing or not applied in the correct order
```

### Expected behavior

All GFM syntax extensions should be properly registered and applied when parsing markdown content. The constructs should be added to the parser in the correct order so that features like autolinks, task lists, tables, etc. are all recognized.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

The issue appears to be related to how syntax extensions are being registered and ordered during the parsing phase. Some constructs seem to be skipped or not inserted at the right position in the parser's construct list.

---
Repository: /testbed
