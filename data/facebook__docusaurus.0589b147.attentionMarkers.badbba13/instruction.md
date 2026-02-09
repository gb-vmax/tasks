# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it seems to be hanging or entering an infinite loop when processing certain markdown content. The browser tab becomes unresponsive and eventually crashes.

### Reproduction

```js
import { remark } from 'remark';

const markdown = `
This is **bold** and this is *italic* text.
`;

const processor = remark();
const result = processor.processSync(markdown);
// Browser becomes unresponsive here
console.log(result);
```

### Expected behavior

The markdown should be parsed successfully without causing the page to hang or crash. The parser should return the processed result in a reasonable amount of time.

### System Info
- remark version: 15.0.1
- Browser: Chrome 120
- OS: Windows 11

This seems to have started happening recently. The same code was working fine before. Any markdown with emphasis markers (asterisks, underscores) seems to trigger this behavior.

---
Repository: /testbed
