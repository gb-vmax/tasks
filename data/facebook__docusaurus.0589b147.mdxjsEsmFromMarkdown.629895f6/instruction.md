# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where ESM imports/exports in MDX files are not being processed correctly. The parser seems to be handling the enter/exit events for `mdxjsEsm` nodes in the wrong order, causing the AST to be malformed.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
export const foo = 'bar'

# Hello World
`

const result = await compile(mdxContent)
// The compiled output is incorrect or throws an error
```

### Expected behavior

The MDX compiler should correctly parse and handle ESM import/export statements at the top of MDX files. The AST should be properly constructed with `mdxjsEsm` nodes in the correct positions.

### Additional context

This appears to affect any MDX file that contains `export` or `import` statements. The parsing seems to get confused and doesn't properly enter/exit the ESM nodes during the markdown-to-AST transformation.

---
Repository: /testbed
