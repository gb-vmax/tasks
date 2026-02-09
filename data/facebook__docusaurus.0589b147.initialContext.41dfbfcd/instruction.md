# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with parsing MDX content. The parser seems to be failing on basic MDX syntax that previously worked fine.

### Reproduction

```js
const mdxContent = `
# Hello World

<MyComponent />
`;

// Parser fails to initialize correctly
const result = parse(mdxContent);
```

When trying to parse even simple MDX documents, the parser context appears to be incorrectly initialized, causing unexpected parsing behavior or errors.

### Expected behavior

The MDX parser should correctly handle basic MDX syntax including JSX components mixed with markdown content. The parser context should be properly initialized to handle block-level statements.

### Additional context

This seems to have started happening recently. The parser's initial context state might not be set up correctly, affecting how it processes the document from the start.

---
Repository: /testbed
