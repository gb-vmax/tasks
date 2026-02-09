# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link and image parsing where the end position of labels is being calculated incorrectly. This causes problems when trying to process or extract information from markdown links and images in MDX content.

### Reproduction

```js
// When parsing MDX content with links or images like:
const mdxContent = `
[Link text](url)
![Image alt](image-url)
`

// The label end position is off by one event
// This affects any tooling that relies on accurate position information
```

### Expected behavior

The parser should correctly identify the end position of link/image labels. The label group's end position should align with the actual end of the label syntax in the source text.

### Additional context

This seems to affect both link and image types since they share the same resolution logic. The position offset appears to be calculating one event too far when determining the label boundaries.

---
Repository: /testbed
