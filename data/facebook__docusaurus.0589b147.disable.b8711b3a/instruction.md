# Bug Report

### Describe the bug

After a recent update, MDX parsing is completely broken. When trying to parse any MDX content, I'm getting errors about `disable` being undefined or not a function. This is affecting all of my MDX files and completely breaking the build.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This throws an error
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without errors. The `disable` export should be available and functional as it was in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening very recently, possibly after a dependency update. The error suggests that something is wrong with the `disable` export in the constructs module.

---
Repository: /testbed
