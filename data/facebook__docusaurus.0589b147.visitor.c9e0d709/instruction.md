# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-gfm plugin where text replacement and finding operations seem to get stuck in an infinite loop or fail to process nodes correctly. The browser tab becomes unresponsive when processing markdown content with certain patterns.

### Reproduction

```js
import remarkGfm from 'remark-gfm'
import { unified } from 'unified'
import remarkParse from 'remark-parse'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const markdown = `
This is some text with **bold** and _italic_.

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
`

// Processing hangs or produces incorrect output
const result = processor.processSync(markdown)
```

### Expected behavior

The markdown should be parsed correctly without hanging, and text nodes should be properly traversed and processed. The find and replace functionality should work as expected for GFM features like tables, strikethrough, etc.

### Additional context

This seems to happen specifically when the plugin tries to process text nodes within nested structures. The issue appeared after a recent update to the vendor file.

---
Repository: /testbed
