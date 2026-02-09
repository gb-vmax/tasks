# Bug Report

### Describe the bug

After a recent update, the MDX parser appears to be broken. When trying to process MDX files, the tokenizer seems to be incomplete or corrupted, causing parsing to fail entirely.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX file.
`

// This fails to parse
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should be compiled successfully without errors. The tokenizer should properly handle the markdown syntax and return the compiled output.

### Additional context

This seems to have started happening after the latest changes. The tokenizer factory function appears to be cut off or incomplete, which is preventing any MDX content from being processed. Even the simplest markdown content fails to compile.

---
Repository: /testbed
