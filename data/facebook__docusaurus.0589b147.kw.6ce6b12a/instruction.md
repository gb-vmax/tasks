# Bug Report

### Describe the bug

After a recent update, the MDX parser seems to be broken. When trying to parse MDX files, the tokenizer fails to properly recognize keywords and the parser throws errors or produces incorrect output.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

export const foo = 'bar'

Some content here.
`

const result = await compile(mdxContent)
// Parser fails or produces unexpected results
```

### Expected behavior

The MDX content should be parsed correctly and keywords should be properly tokenized. The compiler should return valid output without errors.

### Additional context

This appears to have started after updating to the latest version. The keyword tokenization seems to be affected - keywords like `export`, `import`, `const`, etc. are not being handled properly during the parsing phase.

---
Repository: /testbed
