# Bug Report

### Describe the bug

I'm experiencing incorrect indentation behavior when working with MDX content. The indentation depth seems to be calculated incorrectly, resulting in malformed output with extra spaces or missing indentation where it should be present.

### Reproduction

```js
// When processing MDX with nested elements
const mdxContent = `
<Component>
  <NestedComponent>
    Content here
  </NestedComponent>
</Component>
`

// The output indentation doesn't match the expected depth
// Extra indentation is added or indentation is completely missing
```

### Expected behavior

The indentation should correctly reflect the nesting depth of elements. Each level of nesting should add consistent indentation, and the first level shouldn't have empty indentation.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
