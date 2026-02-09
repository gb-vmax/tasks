# Bug Report

### Describe the bug

I'm experiencing an issue with blank line detection in markdown parsing. When I have markdown content with spaces at the beginning of blank lines, the parser doesn't recognize them correctly anymore.

### Reproduction

```js
const markdown = `
First paragraph

  
Second paragraph
`

// The blank line with leading spaces is not being recognized properly
// This causes parsing errors or unexpected behavior
```

When there are leading spaces on what should be a blank line, the parser seems to be handling them incorrectly. It looks like the logic for detecting blank lines with whitespace prefixes got inverted somehow.

### Expected behavior

Blank lines with leading whitespace should still be recognized as blank lines and parsed correctly. The markdown should be split into two separate paragraphs.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like it might be a recent regression as it was working fine before. Any help would be appreciated!

---
Repository: /testbed
