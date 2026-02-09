# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content rendering where components are not being processed correctly. It seems like the scope tracking for JSX elements is broken, causing some components to be skipped or not recognized properly.

### Reproduction

```jsx
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<CustomComponent>
  <NestedComponent />
</CustomComponent>

Some text here.
`

const result = await compile(mdxContent, {
  /* options */
})
```

When compiling MDX with nested custom components, the output doesn't include all the expected component references. Some components in the scope seem to be missing from the final output.

### Expected behavior

All custom components used in the MDX content should be properly tracked and included in the compiled output. The scope should correctly identify and process every component reference.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The component tracking logic might have an off-by-one error or the scope initialization is not working as expected.

---
Repository: /testbed
