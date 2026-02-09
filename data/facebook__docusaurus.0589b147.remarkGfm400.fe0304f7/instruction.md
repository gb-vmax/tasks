# Bug Report

### Describe the bug
After a recent update, markdown parsing is completely broken when using GFM (GitHub Flavored Markdown) extensions. The parser fails to correctly process markdown content and produces unexpected output.

### Reproduction
```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkGfm from 'remark-gfm'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const markdown = `
# Test

This is a **test** with some GFM features:

- [ ] Task item
- [x] Completed task

| Column 1 | Column 2 |
|----------|----------|
| Data     | More     |
`

const result = processor.processSync(markdown)
// Parser throws an error or produces malformed output
```

### Expected behavior
The markdown should be parsed correctly with GFM features like task lists and tables working as expected. The processor should handle the content without errors.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems to have started after the latest changes. Previously this was working fine with the same markdown input.

---
Repository: /testbed
