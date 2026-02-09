# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the MDX compiler. It looks like there's some kind of parsing issue with regular expressions or special characters. The error message is pretty cryptic but it seems to be failing during the compilation step.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document with some **bold** text.
`

const result = await compile(mdxContent)
```

When I run this code, I get an error that seems to be coming from the regex parsing logic inside the MDX compiler. It's complaining about an unexpected character or token.

### Expected behavior

The MDX content should compile successfully without any errors. This worked fine in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This just started happening after updating to 3.0.0. Rolling back to the previous version makes everything work again.

---
Repository: /testbed
