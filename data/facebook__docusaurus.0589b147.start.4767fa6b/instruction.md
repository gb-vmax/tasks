# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where whitespace handling seems to be completely broken. Text that should be parsed with proper spacing is now being processed incorrectly, causing the parser to fail or produce unexpected output.

### Reproduction

```js
const remark = require('remark');

const markdown = `
This is a test paragraph.

Another paragraph here.
`;

const result = remark().parse(markdown);
console.log(result);
```

When parsing markdown content with spaces and line breaks, the parser no longer handles whitespace correctly. It seems like the logic for detecting and processing spaces has been inverted somehow.

### Expected behavior

The markdown parser should correctly identify and handle whitespace characters (spaces, tabs, newlines) and process them according to the markdown spec. Spaces should be consumed and processed as space tokens, not skipped entirely.

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to have started happening recently and is breaking markdown parsing for any content with standard spacing. Any help would be appreciated!

---
Repository: /testbed
