# Bug Report

### Describe the bug

The MDX tokenizer appears to be broken after a recent change. When trying to parse MDX content, the parser fails to properly construct and handle token constructs. This affects all MDX parsing functionality.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This fails to compile
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully and return the compiled output. The tokenizer should properly handle constructs and return appropriate states during parsing.

### Additional context

This seems to have started happening recently. The tokenizer's `constructFactory` function appears to be incomplete or corrupted, causing the entire parsing pipeline to fail. Any MDX file, regardless of complexity, cannot be processed.

---
Repository: /testbed
