# Bug Report

### Describe the bug

The `admonitionTitleToDirectiveLabel` function is not correctly handling admonition blocks that are both indented and quoted. When markdown content contains admonitions that are inside blockquotes with indentation, the output has the quote markers and indentation in the wrong order.

### Reproduction

```js
import {admonitionTitleToDirectiveLabel} from '@docusaurus/utils';

const content = `
>   :::note This is a title
>   content
`;

const result = admonitionTitleToDirectiveLabel(content, ['note']);
console.log(result);
```

### Expected behavior

When an admonition is both quoted (with `>`) and indented, the indentation should come before the quote marker in the output to maintain proper markdown structure. Currently, the quote marker is being placed before the indentation, which breaks the formatting.

For example:
```markdown
>   :::note This is a title
```

Should be converted with indentation preserved before the quote marker, not after it.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
