# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in markdown files. When using directives (like `:::note` or similar syntax), the parser seems to crash or produce incorrect output. This appears to be related to how tokens are being processed during the exit phase of parsing.

### Reproduction

```js
import {remarkDirective} from 'remark-directive';
import {unified} from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const markdown = `
:::note
This is a note directive
:::
`;

const result = processor.processSync(markdown);
// Parser fails or produces unexpected output
```

### Expected behavior

The directive should be parsed correctly and the resulting AST should properly represent the directive structure. The parser should exit token processing cleanly without errors.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
