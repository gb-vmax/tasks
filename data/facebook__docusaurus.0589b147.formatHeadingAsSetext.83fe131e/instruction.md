# Bug Report

### Describe the bug
Markdown headings with line breaks are being formatted incorrectly. When a heading contains a hard break or text with newlines, the setext-style formatting (underline with `===` or `---`) is not being applied when it should be.

### Reproduction
```js
const heading = {
  type: 'heading',
  depth: 2,
  children: [
    { type: 'text', value: 'Title with\nline break' }
  ]
}

// Or with a break node
const headingWithBreak = {
  type: 'heading',
  depth: 1,
  children: [
    { type: 'text', value: 'Title' },
    { type: 'break' },
    { type: 'text', value: 'continued' }
  ]
}

// These headings are not being formatted as setext style even when setext option is enabled
```

### Expected behavior
Headings that contain line breaks should be formatted using ATX style (`#` prefix) instead of setext style (underline), since setext doesn't support multi-line headings. The current behavior seems to be doing the opposite - it's trying to use setext for headings with breaks when it shouldn't.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
