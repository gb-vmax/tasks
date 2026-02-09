# Bug Report

### Describe the bug

I'm encountering an issue where MDX processing appears to be failing silently or not handling certain node types correctly. It seems like the handler dispatch logic is broken - handlers that should be called aren't being invoked, and the processing just stops without any error.

### Reproduction

```js
// When processing MDX content with specific node types
const mdxContent = `
# Hello

Some content here
`;

// The handler for heading nodes doesn't get called
// and the content isn't processed as expected
```

I noticed this after a recent update. The MDX compiler seems to be skipping over valid nodes entirely, like it's not recognizing them even though they have the correct structure and properties.

### Expected behavior

The MDX compiler should properly dispatch to the appropriate handlers based on node type. All valid nodes in the AST should be processed by their corresponding handlers.

### Additional context

This appears to affect all node types, not just headings. It's like the handler lookup mechanism is completely inverted or something - nodes that should match don't, and the fallback behavior is also wrong.

---
Repository: /testbed
