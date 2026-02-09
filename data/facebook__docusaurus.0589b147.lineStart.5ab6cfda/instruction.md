# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM blocks where the parser enters an unexpected state when processing markdown line endings. The content after certain line breaks is being incorrectly parsed, causing the MDX block to not terminate properly.

### Reproduction

```mdx
export const foo = 'bar'

Some content here
```

When parsing this MDX content, the parser doesn't properly handle the transition from the export statement to regular markdown content. The `mdxjsEsmData` state is entered even when it shouldn't be, leading to incorrect parsing behavior.

### Expected behavior

The parser should correctly identify when an ESM block ends and regular markdown content begins. Line endings should be properly checked before entering the data state, and the parser should only continue processing ESM content when appropriate.

### Additional context

This seems to affect MDX files that have export statements followed by regular markdown content. The issue appears to be related to how line endings are being validated in the state machine.

---
Repository: /testbed
