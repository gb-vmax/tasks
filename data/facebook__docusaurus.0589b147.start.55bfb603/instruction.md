# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the opening bracket of a label is not being processed correctly. The directive syntax seems to be broken and labels are not being recognized properly.

### Reproduction

```js
// Using a directive with a label
:directive[label text]{attributes}

// The label parsing fails and the directive is not recognized
```

When trying to use directives with labels, the parser doesn't seem to be entering/exiting the correct token types. The label marker isn't being handled properly at the start of the label, causing the entire directive to fail parsing.

### Expected behavior

The directive label should be parsed correctly with proper token type handling. The opening bracket should mark the start of the label and the directive should be recognized.

### System Info
- remark-directive version: 3.0.0
- Node version: latest

---
Repository: /testbed
