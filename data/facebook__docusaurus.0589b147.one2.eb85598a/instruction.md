# Bug Report

### Describe the bug

After a recent update, HTML serialization is completely broken. When trying to convert AST nodes to HTML strings, nothing is being output. The rehype-stringify processor seems to fail silently without producing any HTML.

### Reproduction

```js
import {unified} from 'unified'
import rehypeParse from 'rehype-parse'
import rehypeStringify from 'rehype-stringify'

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const html = '<div><p>Hello world</p></div>'
const result = await processor.process(html)

console.log(String(result))
// Expected: '<div><p>Hello world</p></div>'
// Actual: '' (empty string)
```

### Expected behavior

The processor should serialize the AST back to HTML string format. All node types (elements, text, comments, etc.) should be properly converted to their HTML representation.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

This is blocking our entire documentation generation pipeline. Any help would be appreciated!

---
Repository: /testbed
