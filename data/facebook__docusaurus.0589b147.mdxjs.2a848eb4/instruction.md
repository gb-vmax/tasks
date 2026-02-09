# Bug Report

### Describe the bug

After a recent update, MDX parsing seems to be broken. The order of plugins appears to have changed, which is causing markdown content to not be processed correctly in MDX files.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a paragraph with **bold** text.

<CustomComponent />
`

const result = await compile(mdxContent)
// Markdown syntax is not being transformed properly
```

### Expected behavior

The markdown syntax (headers, bold text, etc.) should be parsed and transformed before JSX components are processed. Currently it seems like the markdown transformer is being applied in the wrong order, causing markdown syntax to either not be processed or to interfere with JSX parsing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
