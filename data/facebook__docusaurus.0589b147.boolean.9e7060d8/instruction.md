# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX compiler. The error appears to be coming from the vendored `@mdx-js/mdx` package and is preventing any MDX files from being processed.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This throws a syntax error
const result = await compile(mdxContent)
```

### Error message

The code fails to parse with a syntax error related to property exports in the types module. It seems like there's malformed JavaScript in the vendored version of the library.

### Expected behavior

The MDX content should compile successfully without any syntax errors.

### System Info
- Version: Latest from main branch
- Node.js: 18.x

This is blocking our build process. Any help would be appreciated!

---
Repository: /testbed
