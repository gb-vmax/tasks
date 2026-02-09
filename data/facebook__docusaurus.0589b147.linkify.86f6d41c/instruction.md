# Bug Report

### Describe the bug

The markdown linkification process is not working correctly - links in markdown files are not being converted to their proper permalinks. The original file content is being returned unchanged instead of the processed content with updated links.

### Reproduction

```js
// Given a markdown file with relative links
const markdown = `
Check out [this page](./other-page.md)
And [another one](../docs/guide.md)
`;

const result = linkify(markdown, filePath, {
  siteDir,
  sourceToPermalink,
  onBrokenMarkdownLink: (link) => console.log('Broken:', link)
});

// Expected: Links should be transformed to permalinks
// Actual: Original markdown is returned unchanged
console.log(result); // Still shows "./other-page.md" instead of permalink
```

### Expected behavior

The `linkify` function should process the markdown content and replace relative markdown links with their corresponding permalinks. The returned content should have all links properly transformed.

### Additional context

This appears to affect all markdown link processing in docs. Links that should be converted to their final permalink URLs are being left in their original relative form, which breaks navigation when the site is built.

---
Repository: /testbed
