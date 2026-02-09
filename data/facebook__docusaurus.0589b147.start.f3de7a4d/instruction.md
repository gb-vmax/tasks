# Bug Report

### Describe the bug

I'm encountering an issue with link parsing in markdown. When processing links with label markers, the parser seems to get stuck in an infinite loop or doesn't properly exit the marker state.

### Reproduction

```js
const markdown = '[example](https://example.com)'

// Parser hangs or behaves unexpectedly when processing this
const result = remark.parse(markdown)
```

The issue appears to be related to how label markers are tokenized. After processing a label marker character, the parser doesn't transition to the next state correctly.

### Expected behavior

Links should be parsed correctly without hanging. The label marker should be properly entered and exited, then move on to process the rest of the link syntax.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
