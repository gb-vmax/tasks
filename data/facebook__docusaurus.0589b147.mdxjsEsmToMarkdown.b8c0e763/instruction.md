# Bug Report

### Describe the bug
After a recent update, MDX ESM imports/exports are not being serialized correctly when converting back to markdown. The markdown output appears to be missing the ESM blocks entirely.

### Reproduction
```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkMdx from 'remark-mdx'
import remarkStringify from 'remark-stringify'

const input = `
import { Component } from './Component'

# Hello World
`

const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(remarkStringify)

const result = processor.processSync(input)
console.log(result.toString())
// Expected: Should include the import statement
// Actual: Import statement is missing from output
```

### Expected behavior
When processing MDX content that contains ESM imports/exports, the markdown stringifier should preserve these blocks in the output.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
