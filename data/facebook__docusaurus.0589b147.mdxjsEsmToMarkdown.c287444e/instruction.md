# Bug Report

### Describe the bug
After a recent update, MDX ESM imports/exports are not being serialized correctly when converting back to markdown. The output is missing the ESM code blocks entirely.

### Reproduction
```js
import { someFunction } from './utils'

export const metadata = {
  title: 'My Page'
}

# My MDX Content

This should include the ESM imports/exports above.
```

When processing this MDX content and converting it back to markdown format, the `import` and `export` statements disappear from the output.

### Expected behavior
The ESM import/export statements should be preserved in the markdown output, just like they are in the input.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
