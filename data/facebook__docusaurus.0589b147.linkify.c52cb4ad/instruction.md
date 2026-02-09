# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown linkify function where it's not properly processing markdown content when there are no broken links. The function appears to be returning the original file content instead of the processed content in certain cases.

### Reproduction

```js
// When processing markdown with valid links
const markdown = `
# My Document

Check out [this link](./valid-page.md) and [another link](./other-page.md)
`;

const result = linkify(markdown, filePath, {
  siteDir,
  sourceToPermalink,
  onBrokenMarkdownLink: (link) => console.log('Broken:', link)
});

// Expected: Processed markdown with converted links
// Actual: Original markdown content unchanged
```

### Expected behavior

The linkify function should always return the processed markdown content with converted links, regardless of whether broken links are detected or not. Valid markdown links should be transformed to their permalink equivalents.

### Additional context

This seems to happen specifically when all links in the document are valid. If there are broken links present, the processing works as expected (though only some broken links are being reported, not all of them).

---
Repository: /testbed
