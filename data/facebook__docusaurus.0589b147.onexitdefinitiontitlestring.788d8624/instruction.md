# Bug Report

### Describe the bug
When parsing markdown with reference-style links that include titles, the title information is not being properly captured. The link definitions appear to work but the title attribute is missing from the parsed output.

### Reproduction
```js
const markdown = `
[example]: https://example.com "Example Title"

This is a [example] link.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The title is missing from the definition
console.log(result.definitions.example.title); // undefined
```

### Expected behavior
The parser should capture and store the title string from reference-style link definitions. The title should be accessible in the parsed output structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
