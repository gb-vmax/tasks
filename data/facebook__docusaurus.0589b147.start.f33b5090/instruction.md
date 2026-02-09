# Bug Report

### Describe the bug

I'm experiencing an issue with nested container parsing in markdown documents. When processing documents with multiple levels of nested containers (like nested blockquotes or lists), the parser appears to be handling continuation checks incorrectly, which causes unexpected behavior in how nested structures are recognized and processed.

### Reproduction

```js
const markdown = `
> outer blockquote
> > nested blockquote
> > still nested
> back to outer
`;

// Parse the markdown
const result = remark.parse(markdown);

// The nested structure is not being maintained correctly
// Inner blockquote continuation is not properly detected
```

### Expected behavior

The parser should correctly maintain the nesting hierarchy and properly detect when we're continuing within a nested container versus exiting back to a parent container. Each level of nesting should be handled independently with proper continuation detection.

### Additional context

This seems to affect any markdown structure that uses nested containers - nested blockquotes, nested lists, or combinations thereof. The issue appears to be related to how the document continuation logic determines whether to stay in the current container or check for new containers.

---
Repository: /testbed
