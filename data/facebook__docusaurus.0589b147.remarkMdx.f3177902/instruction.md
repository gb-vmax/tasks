# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the markdown extensions seem to be getting mixed up. When I try to process MDX content, I'm getting unexpected behavior - it seems like the parser is trying to use the wrong extension handlers.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

<CustomComponent />

Some text with **bold** and *italic*.
`

const result = await compile(mdxContent)
// Getting errors or unexpected output
```

### Expected behavior

The MDX content should compile correctly with both markdown syntax and JSX components being properly processed. The extensions should be applied in the correct order and to the correct processing stages.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like the extension registration might be getting confused somewhere in the plugin setup. The markdown-to-AST and AST-to-markdown transformations don't seem to be using the right handlers.

---
Repository: /testbed
