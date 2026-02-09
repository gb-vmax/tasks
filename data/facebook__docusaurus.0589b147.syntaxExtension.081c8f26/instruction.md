# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-gfm syntax extension system after a recent update. When trying to use GFM (GitHub Flavored Markdown) features, the parser seems to be completely broken and doesn't process markdown correctly anymore.

### Reproduction

```js
import remarkGfm from 'remark-gfm'
import { unified } from 'unified'
import remarkParse from 'remark-parse'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const markdown = `
# Test

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

- [x] Task 1
- [ ] Task 2
`

const result = processor.processSync(markdown)
// Parser crashes or produces unexpected output
```

### Expected behavior

The GFM syntax extensions (tables, task lists, etc.) should be properly registered and the markdown should parse correctly without errors.

### Additional context

This seems to have started happening recently. The extension registration mechanism appears to not be working as expected - hooks aren't being properly combined or registered. When I try to parse any GFM-specific syntax, it either fails completely or doesn't recognize the GFM features at all.

---
Repository: /testbed
