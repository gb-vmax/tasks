# Bug Report

### Describe the bug

After a recent update, MDX JSX parsing is completely broken. When trying to parse MDX files with JSX components, the parser fails to process them correctly.

### Reproduction

```js
import { mdxJsx } from 'remark-mdx';

const processor = unified()
  .use(remarkParse)
  .use(mdxJsx, {
    acorn: acornParser,
    addResult: true
  });

// Try to parse MDX with JSX
const result = processor.processSync(`
# Hello

<MyComponent prop="value" />
`);
```

The parser now throws errors or fails to recognize JSX syntax that was previously working fine.

### Expected behavior

MDX files with JSX components should be parsed correctly. The `acorn` option should be used when provided, and the `addResult` callback should be properly passed through to the JSX flow and text parsers.

### Additional context

This appears to have started happening recently. The same code was working in previous versions. It seems like there might be an issue with how the acorn parser instance is being validated or how options are being passed to the internal parsers.

---
Repository: /testbed
