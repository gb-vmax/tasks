# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where it seems to be breaking when trying to process markdown content. The parser initialization appears to have changed and is now causing errors when attempting to parse MDX files.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This now throws an error or produces unexpected behavior
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without errors. The parser should initialize properly and process the markdown/MDX syntax as it did before.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The parser used to work fine with the same content, but now it's failing during the initialization phase.

---
Repository: /testbed
