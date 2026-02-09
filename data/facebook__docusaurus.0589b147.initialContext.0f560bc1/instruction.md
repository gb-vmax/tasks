# Bug Report

### Describe the bug

I'm experiencing a crash when trying to parse MDX files. The parser is throwing an error about `types.b_stat` not being a function. This seems to be breaking the entire parsing pipeline.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX file.
`

// This throws an error
await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without errors. The parser should initialize its context properly and process the file.

### Error message

```
TypeError: types.b_stat is not a function
```

This started happening recently and I'm not sure what changed. The parser seems to be trying to call `types.b_stat` as a function during initialization, but it's not callable.

---
Repository: /testbed
