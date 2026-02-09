# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM imports where the parser seems to be consuming characters incorrectly when processing export/import statements. The problem appears to be related to how line endings are handled in ESM blocks.

### Reproduction

```mdx
export const foo = 'bar'

# Hello World

Some content here
```

When parsing this MDX content, the export statement gets mangled or characters appear in unexpected places. It seems like the parser is consuming a character before checking if it's a line ending, which causes the state machine to behave incorrectly.

### Expected behavior

The ESM export statement should be parsed cleanly without any character corruption. The parser should properly handle line endings in ESM blocks and exit the data state at the correct position.

### Additional context

This seems to affect any MDX file with ESM imports/exports at the top. The issue is subtle but causes parsing errors in certain edge cases, particularly around line boundaries in the ESM block.

---
Repository: /testbed
