# Bug Report

### Describe the bug
I'm encountering an issue with ATX heading parsing where the heading structure seems to be malformed. The parser appears to be entering the heading sequence state incorrectly, which causes downstream processing issues.

### Reproduction
```js
// Parse markdown with ATX headings
const markdown = `
# Heading 1
## Heading 2
### Heading 3
`;

const result = parse(markdown);
// The heading tokens are not structured correctly
```

When parsing ATX-style headings (the ones with `#` symbols), the token structure doesn't match what's expected. It looks like the heading sequence is being entered before the heading itself is properly initialized.

### Expected behavior
The parser should correctly tokenize ATX headings with the proper nesting structure:
1. Enter `atxHeading`
2. Enter `atxHeadingSequence`
3. Process the heading content
4. Exit properly

Instead, it seems to be skipping or reordering these steps.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking markdown parsing for documents with ATX-style headings. Any help would be appreciated!

---
Repository: /testbed
