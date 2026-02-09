# Bug Report

### Describe the bug

I'm experiencing an issue where custom data attributes are not being properly applied to `<pre>` elements when rendering code blocks. The data seems to be getting lost or applied to the wrong element in the tree.

### Reproduction

When processing markdown code blocks with custom metadata/data, the resulting HTML structure doesn't have the data attributes on the `<pre>` tag where they should be.

```js
// Input markdown with code block
const markdown = `
\`\`\`js
console.log('test');
\`\`\`
`;

// After processing, the <pre> element is missing the expected data attributes
// that should have been applied from the node data
```

### Expected behavior

Custom data attributes should be applied to the `<pre>` wrapper element, not just the inner `<code>` element. The data transformation should happen after the full element structure is created.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
