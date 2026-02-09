# Bug Report

### Describe the bug

I'm experiencing an issue with text formatting in markdown output where whitespace/spacing between inline elements is not being handled correctly. When I have multiple inline elements (like emphasis, strong, code, etc.) next to each other, the spacing between them seems off or missing entirely.

### Reproduction

```js
// Example markdown with adjacent inline elements
const markdown = 'This is **bold** _italic_ text'

// When processed, the output doesn't preserve proper spacing
// between the inline elements
```

The issue appears to affect scenarios where you have consecutive phrasing content (inline elements) in a container. The spacing logic seems to be checking boundaries incorrectly, causing it to miss or improperly handle whitespace between adjacent elements.

### Expected behavior

Adjacent inline elements should maintain proper spacing between them. The output should correctly preserve whitespace that exists between different inline formatting elements.

For example:
- `**bold** _italic_` should have space between bold and italic
- Multiple consecutive inline elements should each be properly spaced

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
