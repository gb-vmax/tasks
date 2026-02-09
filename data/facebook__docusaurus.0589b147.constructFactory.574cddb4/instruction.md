# Bug Report

### Describe the bug

After a recent update, the MDX parser appears to be broken and throws syntax errors during compilation. The tokenizer seems to be incomplete or corrupted, causing the entire parsing pipeline to fail.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This throws an error
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any syntax errors. The parser should tokenize and process the content normally.

### Additional context

This seems to have started happening suddenly. The error appears to be related to the tokenizer factory function being incomplete or malformed. The compilation fails immediately when trying to parse any MDX content, even the simplest documents.

---
Repository: /testbed
