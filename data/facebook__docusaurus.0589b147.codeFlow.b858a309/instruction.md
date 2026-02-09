# Bug Report

### Describe the bug

I'm experiencing an issue with code block parsing in markdown. When I try to parse fenced code blocks (triple backticks), the resulting AST nodes are malformed. The `type` field is empty and the `value` is `null` instead of containing the actual code content.

### Reproduction

```js
import {remark} from 'remark';

const markdown = `
\`\`\`javascript
console.log('hello world');
\`\`\`
`;

const result = remark().parse(markdown);
console.log(result.children[0]);
// Expected: { type: 'code', lang: 'javascript', meta: null, value: "console.log('hello world');" }
// Actual: { type: '', lang: 'javascript', meta: null, value: null }
```

The code block node has an empty `type` field and `null` value, which breaks any further processing of the AST.

### Expected behavior

Code block nodes should have:
- `type: "code"`
- `value` containing the actual code content as a string
- Proper `lang` and `meta` fields

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
