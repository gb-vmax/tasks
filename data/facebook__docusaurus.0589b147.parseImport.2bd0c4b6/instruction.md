# Bug Report

### Describe the bug

After a recent update, MDX import statements are no longer being parsed correctly. The parser seems to be completely broken for import declarations, causing any MDX file with imports to fail.

### Reproduction

```mdx
import { Component } from './component'

# My Document

Some content here
```

When trying to parse this MDX content, the parser throws an error or produces invalid output. The issue appears to affect all types of import statements:

- Named imports: `import { foo } from 'bar'`
- Default imports: `import foo from 'bar'`  
- Side-effect imports: `import 'styles.css'`
- Namespace imports: `import * as foo from 'bar'`

### Expected behavior

Import statements should be parsed successfully and the MDX content should render without errors. This was working fine in previous versions.

### System Info

- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to use any MDX files with imports. Any help would be appreciated!

---
Repository: /testbed
