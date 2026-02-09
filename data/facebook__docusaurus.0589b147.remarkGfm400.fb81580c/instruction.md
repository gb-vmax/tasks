# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-gfm plugin where markdown extensions aren't being applied correctly. It seems like the `fromMarkdownExtensions` is not being initialized properly, which causes markdown parsing to fail or behave unexpectedly.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkGfm from 'remark-gfm'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

// Try to parse GFM markdown
const result = processor.processSync('~~strikethrough~~')
```

### Expected behavior

The GFM markdown features (like strikethrough, tables, task lists, etc.) should be parsed correctly. The `fromMarkdownExtensions` should be properly initialized from `data.fromMarkdownExtensions` and not accidentally reference `data.micromarkExtensions`.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have broken after a recent update. The extensions aren't being registered correctly which prevents proper markdown parsing.

---
Repository: /testbed
