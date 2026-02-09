# Bug Report

### Describe the bug

After a recent update, MDX compilation seems to be broken. When trying to compile MDX files, the output is not what I expect - instead of getting the compiled result, I'm getting a function back.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test MDX file.
`

const result = await compile(mdxSource)
console.log(result) // Expected: compiled code, Got: function
```

### Expected behavior

The `compile` function should return the compiled MDX output directly, not wrapped in an additional function. This worked fine in previous versions but broke after the latest update.

### Additional context

This is affecting my build pipeline where I need to process MDX files. The compilation step now returns an unexpected type and I can't access the actual compiled content.

---
Repository: /testbed
