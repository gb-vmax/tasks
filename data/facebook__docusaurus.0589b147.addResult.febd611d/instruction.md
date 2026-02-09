# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where content is being duplicated or appearing in the wrong order after processing. It seems like events are being inserted at the wrong position in the event stream, causing the final output to be corrupted.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Heading

Some paragraph text.

Another paragraph.
`

const result = await compile(mdxContent)
console.log(result)
```

When parsing MDX documents with multiple elements, the output shows duplicated content or elements appearing out of order. For example, paragraphs might appear before headings even though they come after in the source.

### Expected behavior

The parsed MDX should maintain the correct order of elements as they appear in the source document. Events should be inserted at the correct position in the event stream without duplication.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The tokenizer appears to be processing constructs but the results aren't being added to the event stream correctly.

---
Repository: /testbed
