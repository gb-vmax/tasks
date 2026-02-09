# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be hanging or entering an infinite loop when processing certain markdown content. The application becomes unresponsive and eventually times out.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Test Document

Some text with **bold** and _italic_.

- List item 1
- List item 2
`

// This hangs indefinitely
await compile(mdxContent)
```

### Expected behavior

The MDX content should be compiled successfully without hanging. The parser should process the markdown and return the compiled output in a reasonable amount of time.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to specific markdown patterns or a more general parsing issue.

---
Repository: /testbed
