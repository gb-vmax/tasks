# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX parser. It looks like there's an issue with the `constructs_exports` object definition where a function declaration is inserted in the middle of the export statement.

### Reproduction

```js
import { compile } from '@mdx-js/mdx';

const mdxContent = `
# Hello World

This is a test document.
`;

// This throws a syntax error
const result = await compile(mdxContent);
```

### Expected behavior

The MDX content should compile successfully without any syntax errors. The `constructs_exports` object should be properly structured and all exports should be accessible.

### Error

The code fails to parse because there's a function declaration (`const createContentManager = ...`) inserted between the export statement and the actual property definitions. This breaks the object literal syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
