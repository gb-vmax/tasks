# Bug Report

### Describe the bug

I'm experiencing an issue with paragraph rendering where the content inside paragraphs is not being displayed. When converting markdown to HTML, paragraph elements are being created but they appear empty even though the source markdown contains text.

### Reproduction

```js
const markdown = `
This is a paragraph with some text.

Another paragraph here.
`;

// After conversion, paragraphs are empty
// Expected: <p>This is a paragraph with some text.</p>
// Actual: <p></p>
```

When I inspect the generated HTML, I see `<p></p>` tags being created but with no children/content inside them. The paragraph structure is there but all the text content is missing.

### Expected behavior

Paragraphs should contain their text content and inline elements. The children should be properly processed and included in the resulting paragraph element.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
