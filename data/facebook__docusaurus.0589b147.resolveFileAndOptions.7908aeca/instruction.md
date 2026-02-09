# Bug Report

### Describe the bug

When explicitly setting `format: "md"` or `format: "mdx"` in the options, the format is being ignored and instead determined by the file extension. This means that even when I explicitly specify which format to use, the library falls back to checking the file extension against `mdExtensions`.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// Explicitly set format to "mdx"
const result = await compile(
  '# Hello',
  { 
    format: 'mdx'  // This should force MDX format
  }
)

// The format gets overridden based on file extension
// instead of respecting the explicit format option
```

### Expected behavior

When I explicitly provide `format: "md"` or `format: "mdx"` in the options, that format should be used regardless of the file extension. The file extension check should only be used as a fallback when no format is specified.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
