# Bug Report

### Describe the bug

I'm encountering an issue with markdown link and image parsing where the children/alt text is being assigned to the wrong node type. It seems like links are getting alt text assigned to them and images are getting children assigned instead of alt text, which is the opposite of what should happen.

### Reproduction

```js
// Parsing a markdown link
const linkMarkdown = '[link text](url)';
// Expected: node.children should contain the link text
// Actual: node.alt is being set instead

// Parsing a markdown image
const imageMarkdown = '![alt text](url)';
// Expected: node.alt should contain the alt text
// Actual: node.children is being set instead
```

When processing labels in markdown (the text inside `[]`), the parser is assigning the content to the wrong property based on the node type. Links should have `children` populated with the fragment children, while images should have `alt` populated with the text value.

### Expected behavior

- Link nodes (`type === "link"`) should have their `children` property set to the fragment children
- Image nodes (non-link reference nodes) should have their `alt` property set to the text value

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

---
Repository: /testbed
