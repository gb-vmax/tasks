# Bug Report

### Describe the bug

I'm experiencing an issue with nested brackets in directive labels. When using directives with labels that contain newlines, the balance tracking seems to be off and the closing bracket isn't detected correctly.

### Reproduction

```js
// This directive with a newline in the label doesn't parse correctly
const input = `::directive[label with
newline content]`

// The closing bracket ] is not properly recognized
// Balance counter appears to be decremented at the wrong time
```

### Expected behavior

Directives with labels containing newlines should parse correctly and the closing bracket should be properly detected. The balance counter should track opening `[` and closing `]` brackets accurately throughout the label content, including when there are line breaks.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark

---
Repository: /testbed
