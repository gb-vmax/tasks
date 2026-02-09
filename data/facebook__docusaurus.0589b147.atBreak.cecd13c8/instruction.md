# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where content that should be recognized as a break/boundary is not being properly detected. This seems to affect how the parser handles certain code boundaries and construct transitions.

### Reproduction

When parsing MDX content with specific code structures, the parser fails to recognize valid break points. This appears to happen when:

1. Processing content with null code values
2. Evaluating construct boundaries in the tokenizer

Example scenario:
```js
// MDX content with embedded code blocks or specific construct patterns
const mdxContent = `
# Title

Some content here

\`\`\`js
code block
\`\`\`

More content
`;

// Parser doesn't correctly identify breaks between constructs
```

### Expected behavior

The parser should correctly identify break points and construct boundaries, properly recognizing when code values are null and when constructs should transition. Currently, valid break points are being missed, which affects the overall parsing behavior.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started recently and is affecting content that previously parsed correctly. Any insights would be appreciated!

---
Repository: /testbed
