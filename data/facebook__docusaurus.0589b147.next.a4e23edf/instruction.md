# Bug Report

### Describe the bug

I'm experiencing an issue with the remark markdown processor where it seems to be processing content incorrectly or getting stuck in an infinite loop. The processor either hangs indefinitely or produces unexpected output when chaining multiple transformations together.

### Reproduction

```js
import { remark } from 'remark'
import remarkGfm from 'remark-gfm'
import remarkHtml from 'remark-html'

const processor = remark()
  .use(remarkGfm)
  .use(remarkHtml)

const markdown = `
# Hello

This is a test with **bold** text.
`

// This either hangs or produces incorrect output
const result = await processor.process(markdown)
console.log(result.toString())
```

### Expected behavior

The markdown should be processed through the plugin chain correctly and produce valid HTML output. Each plugin in the chain should receive the output from the previous plugin and process it in order.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have started happening recently. When I use a single plugin it works fine, but chaining multiple plugins together causes issues.

---
Repository: /testbed
