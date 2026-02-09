# Bug Report

### Describe the bug

After a recent update, the MDX parser is completely broken and throws syntax errors during runtime. The tokenizer appears to be corrupted or incomplete, causing the entire parsing process to fail.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This now throws an error
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any syntax errors. The parser should be able to tokenize and process the markdown/JSX content as it did before.

### Additional context

This seems to have started happening suddenly. The error appears to be related to the tokenizer factory function being incomplete or malformed. The parser can't even initialize properly.

---
Repository: /testbed
