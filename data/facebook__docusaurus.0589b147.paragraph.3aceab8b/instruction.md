# Bug Report

### Describe the bug

I'm experiencing an issue with paragraph rendering in MDX where the paragraph content is not being processed correctly. It seems like the children of paragraph elements are not being populated as expected, resulting in empty paragraph tags in the output.

### Reproduction

```js
const mdx = `
This is a paragraph with some text.

Another paragraph here.
`

// Process the MDX
const result = await compile(mdx)

// Expected: Paragraphs with actual content
// Actual: Empty <p></p> tags or incorrect content structure
```

When I compile MDX content that contains paragraphs, the resulting HTML has paragraph elements but they appear to be empty or the children aren't being transferred properly from the AST nodes.

### Expected behavior

Paragraph elements should contain their text content and any inline elements (like emphasis, links, etc.) that were present in the source MDX. The `<p>` tags should wrap the actual content, not be empty.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started recently, possibly after an update. The paragraph handler might not be correctly processing the node children.

---
Repository: /testbed
