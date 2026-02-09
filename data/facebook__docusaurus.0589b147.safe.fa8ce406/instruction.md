# Bug Report

### Describe the bug

I'm experiencing an issue with markdown escaping in remark where certain special characters are not being properly escaped or are causing incorrect output. The escaping logic seems to be skipping characters or producing malformed output when dealing with sequences of special characters.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Example with special characters that should be escaped
const input = 'Text with special chars: *test* and more!';
const result = processor.processSync(input);

// The output is missing expected escapes or has incorrect character positioning
console.log(result.toString());
```

When processing markdown with consecutive special characters or specific patterns, the output doesn't match what's expected. Characters that should be escaped are either missing their backslashes or appear in the wrong positions.

### Expected behavior

Special characters should be consistently escaped according to markdown rules, and the output should preserve the correct character positions and escape sequences.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
