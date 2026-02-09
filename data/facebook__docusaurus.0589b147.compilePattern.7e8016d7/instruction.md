# Bug Report

### Describe the bug

When using markdown patterns with the `before` property but without `atBreak`, the pattern matching doesn't work correctly. The regex compilation seems to be creating an unnecessary capture group that interferes with pattern detection.

### Reproduction

```js
const pattern = {
  character: '*',
  before: '\\s',
  after: '\\w',
  atBreak: false
};

// Compile and test the pattern
compilePattern(pattern);
const text = "some *text* here";
const matches = text.match(pattern._compiled);

// Expected to match, but doesn't work as intended
```

### Expected behavior

Patterns with `before` specified should match correctly regardless of whether `atBreak` is true or false. The capture group should only be created when `atBreak` is true, not just when `before` exists.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
