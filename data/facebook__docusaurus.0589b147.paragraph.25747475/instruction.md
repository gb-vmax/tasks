# Bug Report

### Describe the bug

I'm encountering an issue with paragraph rendering in remark-rehype. When processing markdown paragraphs, the children of the resulting HTML element are not being generated correctly. It seems like the wrong node is being passed to `state.all()`, which results in empty or incorrect paragraph content.

### Reproduction

```js
import remarkParse from 'remark-parse';
import remarkRehype from 'remark-rehype';
import { unified } from 'unified';

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

const markdown = `
This is a simple paragraph with some text.
`;

const result = processor.processSync(markdown);
console.log(result);
```

### Expected behavior

The paragraph should contain the text content as children nodes in the resulting HAST (HTML AST). Instead, the paragraph element appears to be empty or contains incorrect children.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
