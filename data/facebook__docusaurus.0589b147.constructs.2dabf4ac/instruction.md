# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where certain syntax constructs are not being recognized or parsed correctly. It seems like some elements that should be processed early in the parsing pipeline are being skipped or processed out of order.

### Reproduction

When parsing MDX content with specific syntax extensions, the parser fails to properly handle constructs that should be added "before" existing ones. This affects the order in which different syntax elements are processed.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

<CustomComponent />

Some text with **bold** and _italic_.
`;

// Parse the content
const result = parseMDX(mdxContent);
// Expected: All syntax constructs processed in correct order
// Actual: Some constructs are missing or processed incorrectly
```

### Expected behavior

All syntax constructs should be registered and processed in the correct order, with "before" constructs being added at the beginning of the processing pipeline and "after" constructs being appended to the end.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently and is affecting our MDX parsing pipeline. Any help would be appreciated!

---
Repository: /testbed
