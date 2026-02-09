# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag parsing where the data handler seems to be calling the wrong methods. When processing MDX content with JSX tags, I'm getting unexpected behavior that appears to be related to how token data is being handled internally.

### Reproduction

```jsx
// MDX content with JSX tags
const mdxContent = `
<CustomComponent data="test">
  Some content here
</CustomComponent>
`

// Process the MDX content
const result = processMdx(mdxContent)
```

When parsing MDX files that contain JSX tags with data attributes, the parser doesn't handle the tokens correctly. The issue seems to occur specifically when the parser encounters data within JSX tags.

### Expected behavior

The MDX parser should correctly process JSX tags and their data attributes without errors. The token handling should properly enter and exit data nodes during the parsing phase.

### System Info

- remark-mdx version: 3.0.0
- Node version: 18.x

Has anyone else run into this? It seems like something changed in how the internal token handlers work.

---
Repository: /testbed
