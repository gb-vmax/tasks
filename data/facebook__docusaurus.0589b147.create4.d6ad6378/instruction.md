# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where tokenization appears to be broken. When parsing MDX content, the parser seems to be passing arguments in the wrong order or calling functions incorrectly during the tokenization phase.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document.
`

// Attempting to compile MDX content
const result = await compile(mdxContent)
```

When running this code, the parser fails to properly tokenize the content. It seems like the internal `createTokenizer` function is receiving its arguments in an unexpected order, causing the parsing to fail or produce incorrect results.

### Expected behavior

The MDX content should be parsed correctly and the tokenizer should be created with the proper arguments in the correct order. The compilation should complete successfully without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
