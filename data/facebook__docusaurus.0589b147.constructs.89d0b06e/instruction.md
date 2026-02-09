# Bug Report

### Describe the bug

I'm encountering an issue with the remark-gfm parser where certain GFM (GitHub Flavored Markdown) constructs are not being processed correctly. It seems like some syntax extensions are either being skipped or applied in the wrong order, causing parsing failures or unexpected output.

### Reproduction

When parsing markdown with multiple GFM extensions enabled, some constructs appear to be missing or incorrectly positioned in the final output. For example:

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .processSync(markdownContent)
```

The issue manifests when there are multiple syntax constructs that need to be registered. Some constructs that should be added to the parser are being skipped, and others are being inserted at the wrong position in the construct list.

### Expected behavior

All GFM syntax extensions should be properly registered and applied in the correct order. The parser should handle all constructs from the list without skipping any elements or inserting them at incorrect positions.

### Additional context

This appears to be related to how constructs are being added to the existing list. The behavior suggests that either:
1. The last construct in the list is being skipped during iteration
2. Constructs are being inserted at the wrong index position

This is causing inconsistent markdown parsing results depending on which GFM features are being used.

---
Repository: /testbed
