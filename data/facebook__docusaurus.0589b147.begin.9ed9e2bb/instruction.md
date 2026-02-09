# Bug Report

### Describe the bug

I'm encountering an issue with parsing markdown titles/headings. When a title is followed immediately by a closing marker without any content, the parser seems to hang or produce incorrect output. The title parsing doesn't complete properly in certain edge cases.

### Reproduction

```js
// Example markdown that triggers the issue:
const markdown = `
# 
Some content here
`

// Or with other heading levels:
const markdown2 = `
## 
Text below
`
```

When parsing markdown with an empty heading (just the marker followed by a space and newline), the parser doesn't handle it correctly. It appears the title parsing state machine gets stuck or doesn't properly exit.

### Expected behavior

The parser should gracefully handle empty headings or headings with only whitespace, either by:
- Treating them as valid (but empty) headings
- Properly exiting the title parsing state and continuing with the rest of the document

Currently it seems like the parser doesn't properly complete the title parsing flow in these cases.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
