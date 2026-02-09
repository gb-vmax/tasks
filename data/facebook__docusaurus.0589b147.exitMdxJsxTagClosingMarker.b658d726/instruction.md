# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag closing markers where the tag data seems to get lost or reset unexpectedly. When processing MDX content with self-closing or closing tags, the parser appears to be creating a new empty tag object instead of using the existing one, which causes the tag's context and properties to be lost.

### Reproduction

```jsx
import { compile } from '@mdx-js/mdx'

const mdxContent = `
<CustomComponent>
  Some content
</CustomComponent>
`

const result = await compile(mdxContent)
// The closing tag doesn't properly reference the opening tag
// Tag close marker doesn't retain the original tag data
```

This also happens with self-closing tags:

```jsx
const mdxContent = `<CustomComponent />`
const result = await compile(mdxContent)
```

### Expected behavior

The closing marker should properly reference and mark the existing tag object as closed, preserving all the tag's data and attributes. The tag context should be maintained throughout the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it might be related to how the tag state is being managed during the exit phase of parsing. Any help would be appreciated!

---
Repository: /testbed
