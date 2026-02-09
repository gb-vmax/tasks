# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the order of processing seems to be affecting the output. After a recent update, MDX documents with both ESM imports and JSX expressions are not being parsed correctly.

### Reproduction

```mdx
import { Component } from './component'

export const metadata = {
  title: 'Test'
}

<Component>
  {someExpression}
</Component>
```

When parsing this MDX content, the expressions inside JSX components are not being handled properly. It seems like the ESM imports/exports and expressions are interfering with each other during the parsing phase.

### Expected behavior

The MDX parser should correctly handle documents that contain:
1. ESM import/export statements at the top
2. JSX components with embedded expressions

Both should be processed independently without conflicts.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
