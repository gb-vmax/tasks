# Bug Report

### Describe the bug

When parsing MDX files with ES module imports/exports, the parser seems to be producing malformed AST nodes. The import/export statements are not being processed correctly and the resulting structure appears to be inverted or corrupted.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
import { Button } from './components'

export const metadata = {
  title: 'Hello'
}

# Hello World
`

const result = await compile(mdxContent)
// The AST for mdxjsEsm nodes appears malformed
```

### Expected behavior

ES module imports and exports in MDX files should be parsed correctly, with proper enter/exit handling during AST traversal. The resulting AST should have correctly structured mdxjsEsm nodes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
