# Bug Report

### Describe the bug

The table of contents generation is producing incorrect output for heading items. When generating TOC entries, heading-type items are being processed with the wrong function, causing them to render incorrectly in the final output.

### Reproduction

```js
// Create a markdown file with headings
const markdown = `
# Main Title
## Section 1
### Subsection 1.1
## Section 2
`;

// Process the markdown to generate TOC
// The TOC output will show incorrect structure for heading items
```

When processing documents with multiple heading levels, the generated table of contents doesn't match the actual document structure. Slice-type items seem to work fine, but heading items are being rendered incorrectly.

### Expected behavior

The TOC should correctly represent the document structure with proper handling of both slice and heading type items. Each heading should be processed according to its type and rendered appropriately in the table of contents.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
