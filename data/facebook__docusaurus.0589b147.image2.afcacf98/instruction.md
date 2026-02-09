# Bug Report

### Describe the bug

After a recent update, image nodes are not being rendered correctly in MDX content. The images appear to be broken or missing entirely when the MDX is compiled.

### Reproduction

```js
const mdx = `
# My Document

![Alt text](https://example.com/image.png "Image title")

Some content here.
`

// Compile the MDX
const result = compile(mdx)

// The image node is not generated correctly
// Expected: type: "image", url: "https://example.com/image.png"
// Actual: type: "img", url: null
```

When compiling MDX content that includes standard markdown image syntax, the resulting AST has incorrect properties. The image URL is coming through as `null` instead of the actual URL value.

### Expected behavior

Images in MDX should compile to proper image nodes with the correct URL and other properties populated. The compiled output should render images as expected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
