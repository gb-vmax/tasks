# Bug Report

### Describe the bug

After a recent update, the MDX image handler is returning the wrong object. When processing markdown images, the handler is now returning the original markdown AST node instead of the transformed HAST element. This breaks the conversion pipeline and causes images to not render properly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Test

![Alt text](image.png "Title")
`

const result = await compile(mdxSource)
// The image node in the output is incorrect
// Expected: HAST element with type "element", tagName "img"
// Actual: Original markdown node
```

### Expected behavior

The image handler should return the transformed HAST element (the `result` object) after applying data and patches. The returned object should have:
- `type: "element"`
- `tagName: "img"`
- `properties` with `src`, `alt`, and `title`
- `children: []`

Instead, it's returning the original markdown node which doesn't have the correct structure for rendering.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
