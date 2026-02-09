# Bug Report

### Describe the bug

After a recent update, MDX parsing is completely broken. Documents that previously parsed correctly are now failing to render, and the output is garbled or throws errors.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

<CustomComponent prop="value" />

Some text with **bold** and _italic_.
`

const result = await compile(mdxContent)
// Result is malformed or throws an error
```

### Expected behavior

MDX documents should parse correctly with proper handling of:
- JSX components
- Markdown syntax
- Mixed content

The parser worked fine in previous versions but now seems to be processing extensions in the wrong order or configuration.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
