# Bug Report

### Describe the bug

After a recent update, I'm getting a runtime error when trying to process markdown content. The application crashes with `TypeError: node is not a function` when attempting to parse any markdown input.

### Reproduction

```js
import { remark } from 'remark';

const markdown = `
# Hello World

This is a test document.
`;

const processor = remark();
const result = processor.processSync(markdown);
// TypeError: node is not a function
```

### Expected behavior

The markdown should be parsed successfully without throwing any errors. This was working fine in the previous version.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken after pulling the latest changes. Any help would be appreciated!

---
Repository: /testbed
