# Bug Report

### Describe the bug

After a recent update, MDX parsing seems to be processing extensions in the wrong order, which is causing issues with how markdown and JSX are being interpreted. I'm seeing unexpected behavior where markdown syntax isn't being properly recognized before JSX parsing happens.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

<CustomComponent />

Some **bold text** here
`

const result = await compile(mdxContent)
```

When compiling MDX content that mixes markdown syntax with JSX components, the markdown elements are not being parsed correctly. It seems like the order of processing has changed and markdown syntax is being evaluated after JSX instead of before, leading to incorrect output.

### Expected behavior

Markdown syntax should be processed first, then JSX components should be handled. The markdown elements like headings and bold text should be properly converted to their HTML equivalents before any JSX transformation occurs.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
