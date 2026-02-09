# Bug Report

### Describe the bug

After a recent update, strikethrough text in GFM (GitHub Flavored Markdown) is not being parsed correctly. The markdown processor seems to be creating nodes with an incorrect structure, which breaks strikethrough rendering.

### Reproduction

```js
import remarkGfm from 'remark-gfm';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm);

const result = processor.parse('~~strikethrough text~~');

// The AST node type is incorrect
console.log(result);
```

When processing markdown with strikethrough syntax (`~~text~~`), the resulting AST has malformed nodes. The strikethrough elements are not being recognized or transformed properly.

### Expected behavior

Strikethrough markdown should be parsed into proper AST nodes with type `"delete"` and the text content should be correctly nested within the children array. The rendered output should display text with a strikethrough style.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
