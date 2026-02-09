# Bug Report

### Describe the bug

I'm encountering an issue with directive text parsing where the condition for checking attributes appears to be inverted. When parsing directive text with code `123` (opening curly brace `{`), the parser is not behaving as expected.

### Reproduction

```js
// When parsing directive text like:
:directive[label]{attribute}

// The parser seems to skip or mishandle the attributes section
// The condition check for code === 123 appears backwards
```

The issue is in the `afterLabel` function where it checks for the opening curly brace character (code 123). The logic seems inverted - it's checking `code === 123` when it should probably be checking `code !== 123`.

### Expected behavior

The parser should correctly attempt to parse attributes when it encounters an opening curly brace (`{`) after the label section of a directive. Currently, the conditional logic appears to be doing the opposite of what's intended.

### System Info
- Package: remark-directive@3.0.0
- Environment: Jest vendor bundle

---
Repository: /testbed
