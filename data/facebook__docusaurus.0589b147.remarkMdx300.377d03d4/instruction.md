# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing after a recent update. It seems like the markdown/MDX content is not being processed correctly - the parser appears to be ignoring certain MDX-specific syntax elements.

### Reproduction

When trying to parse MDX content that includes JSX expressions or components, the output doesn't match what's expected. For example:

```js
import { remark } from 'remark'
import remarkMdx from 'remark-mdx'

const processor = remark().use(remarkMdx)

const mdxContent = `
# Hello

<MyComponent prop="value" />

Some text with {jsxExpression}
`

const result = processor.processSync(mdxContent)
console.log(result)
```

The JSX components and expressions in the MDX content aren't being recognized or transformed properly. The parser seems to be treating them as plain text instead of MDX syntax.

### Expected behavior

The MDX parser should correctly recognize and process JSX components, expressions, and other MDX-specific syntax elements. The micromark extensions should be properly applied during the parsing phase.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
