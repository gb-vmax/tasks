# Bug Report

### Bug Report: MDX text nodes not rendering correctly

I've encountered an issue where text content in MDX files is not being displayed properly. It seems like text nodes are being created with incorrect properties, causing content to disappear or not render at all.

### Reproduction

When processing MDX content with text nodes:

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is some text content that should be visible.
`

const result = await compile(mdxContent)
// Text content is missing or not rendering
```

### Expected behavior

Text nodes should render normally and display their content. The text "This is some text content that should be visible." should appear in the output.

### Actual behavior

Text content seems to be missing or rendering as null/undefined values instead of the actual text.

### Environment

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
