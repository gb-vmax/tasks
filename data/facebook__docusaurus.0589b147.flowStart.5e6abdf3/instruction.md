# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to hang or fail to properly initialize when processing certain documents. The document flow tokenizer doesn't appear to be getting set up correctly, leading to undefined behavior when trying to parse content.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some paragraph text here.
`

// Parser fails or behaves unexpectedly
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should be parsed successfully and the flow tokenizer should be properly initialized for processing the document structure. The compiled output should contain the expected AST representation of the markdown content.

### Additional context

This seems to affect document flow processing specifically. The issue appears when the parser tries to handle the content flow state, and it looks like the child flow tokenizer might not be getting assigned properly during initialization.

---
Repository: /testbed
