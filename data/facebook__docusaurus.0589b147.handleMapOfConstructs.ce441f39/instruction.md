# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain code constructs are not being tokenized correctly. It seems like the tokenizer is failing to handle specific character codes properly, leading to incorrect parsing behavior.

### Reproduction

When processing MDX content with certain special characters or code patterns, the parser doesn't recognize valid constructs and fails to process them as expected.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some text with special characters

\`\`\`js
const code = null;
\`\`\`
`;

// Parse the MDX
const result = compile(mdxContent);
// Expected: Proper parsing of all constructs
// Actual: Some constructs are not recognized
```

### Expected behavior

The tokenizer should correctly identify and handle all valid code constructs, including those with null/special character codes. All defined constructs in the character map should be properly resolved and processed.

### Additional context

This appears to be related to how the tokenizer handles character code lookups in the construct map. The issue manifests when processing content that should match specific character-based constructs but they're being skipped or incorrectly identified.

---
Repository: /testbed
