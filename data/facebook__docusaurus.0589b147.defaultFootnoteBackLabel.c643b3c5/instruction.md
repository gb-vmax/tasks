# Bug Report

### Describe the bug

When using footnotes with multiple references to the same footnote, the back reference labels are generated incorrectly. The label for the second and subsequent references shows the wrong reference number in the suffix.

### Reproduction

```js
// Create MDX content with a footnote referenced multiple times
const mdxContent = `
Here is a reference[^1] and another reference to the same footnote[^1].

[^1]: This is the footnote content.
`;

// Compile and render the MDX
// The back reference links will show incorrect labels
// Expected: "Back to reference 1-2" for the second reference
// Actual: "Back to reference 1-1" for the second reference
```

### Expected behavior

When a footnote is referenced multiple times in the document, each back reference link should have a unique label that correctly identifies which reference it points to. For example:
- First reference: "Back to reference 1"
- Second reference: "Back to reference 1-2"
- Third reference: "Back to reference 1-3"

Currently, all back references after the first one show the same suffix number instead of incrementing properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
