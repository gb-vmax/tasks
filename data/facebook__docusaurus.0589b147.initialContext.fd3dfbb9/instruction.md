# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where it throws a `TypeError` when trying to parse MDX content. The error message indicates that the parser is trying to call array methods on something that isn't an array.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here
`

// This throws an error
await compile(mdxContent)
```

The parser fails with an error like `Cannot read property 'length' of undefined` or similar array-related errors during the parsing phase.

### Expected behavior

The MDX content should parse successfully without throwing any errors. The parser should be able to handle the context stack properly.

### Additional context

This seems to affect basic MDX parsing functionality. Even simple markdown content fails to compile. The issue appears to be related to the parser's context management.

---
Repository: /testbed
