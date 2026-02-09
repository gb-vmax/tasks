# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the first chunk of text content in a paragraph is being assigned the wrong content type. This affects how the content is processed and can lead to incorrect rendering behavior.

### Reproduction

When parsing MDX content with paragraphs, the initial text chunk gets an incorrect `contentType` value. This happens specifically for the first chunk in a paragraph where there's no previous token.

```js
// Example MDX content that triggers the issue
const mdxContent = `
This is a paragraph with text content.
`;

// The first chunkText token is created with contentType based on 
// the previous token state, but the logic seems inverted
```

### Expected behavior

The first text chunk in a paragraph (when there's no previous token) should have the appropriate content type set. Currently it appears the content type assignment logic may be checking the previous token state in the wrong order.

### Additional context

This seems to affect the token chain initialization in the content flow. The issue is in how `contentType` is determined when creating new `chunkText` tokens - the value depends on whether a previous token exists, but the assignment may not be handling the initial case correctly.

---
Repository: /testbed
