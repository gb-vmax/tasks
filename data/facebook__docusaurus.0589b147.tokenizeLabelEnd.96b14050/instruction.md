# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with labels are not being processed correctly. It seems like the parser is either skipping valid links or processing invalid ones when it shouldn't.

### Reproduction

```js
const markdown = `
[valid link][label]

[label]: https://example.com
`

// The link is not being resolved properly
// Or alternatively, invalid links are being processed when they shouldn't be
```

When parsing markdown with reference-style links, the behavior is inconsistent. Sometimes valid links with defined labels aren't being recognized, and other times links that should be ignored are being processed.

### Expected behavior

Reference-style links should be properly resolved when:
1. The link has a valid label syntax `[text][label]`
2. The label is defined somewhere in the document

Links should be ignored/not processed when the label is marked as inactive or doesn't meet the criteria for valid link resolution.

### System Info
- remark version: 15.0.1
- Node version: latest

This seems to have started happening recently and is affecting markdown documents that use reference-style links extensively. Any help would be appreciated!

---
Repository: /testbed
