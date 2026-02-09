# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where fragments are not being properly added to the stack. When processing MDX content with nested components or fragments, the rendered output is missing expected content or appears broken.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<>
  <p>First paragraph</p>
  <p>Second paragraph</p>
</>
`

const result = await compile(mdxContent)
// The compiled output is missing the fragment children
```

### Expected behavior

The fragment and its children should be properly included in the compiled output. All nested elements within fragments should render correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
