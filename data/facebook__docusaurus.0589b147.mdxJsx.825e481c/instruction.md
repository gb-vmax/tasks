# Bug Report

### Describe the bug

When passing custom `acorn` options to the MDX parser, the options are being ignored and not applied correctly. The parser seems to skip the acorn configuration even when a valid acorn instance is provided.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import * as acorn from 'acorn'

const mdxSource = `
# Hello World
<CustomComponent />
`

const result = await compile(mdxSource, {
  acorn: acorn,
  acornOptions: {
    ecmaVersion: 2020,
    sourceType: 'module'
  }
})
```

### Expected behavior

The custom acorn options (like `ecmaVersion: 2020`) should be merged and applied when parsing the MDX content. The parser should respect the configuration passed through `acornOptions`.

### Actual behavior

The acorn options appear to be ignored, and the parser doesn't use the custom configuration. This makes it impossible to customize the JavaScript parsing behavior for MDX files.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
