# Bug Report

### Describe the bug

Markdown headings are being converted to incorrect HTML heading levels when using remark-rehype. All heading levels appear to be shifted up by one (e.g., `# Heading` becomes `<h2>` instead of `<h1>`, `## Heading` becomes `<h3>` instead of `<h2>`, etc.).

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'
import rehypeStringify from 'rehype-stringify'

const markdown = `
# Main Title
## Subtitle
### Section
`

const result = await unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypeStringify)
  .process(markdown)

console.log(String(result))
// Outputs: <h2>Main Title</h2><h3>Subtitle</h3><h4>Section</h4>
```

### Expected behavior

The heading levels should match the markdown input:
- `# Main Title` should convert to `<h1>Main Title</h1>`
- `## Subtitle` should convert to `<h2>Subtitle</h2>`
- `### Section` should convert to `<h3>Section</h3>`

Currently getting h2, h3, h4 instead of h1, h2, h3.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
