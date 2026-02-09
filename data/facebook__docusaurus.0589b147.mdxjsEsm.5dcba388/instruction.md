# Bug Report

### Describe the bug

I'm experiencing an issue with MDX import statements where the parser seems to be incorrectly handling certain cases. When using import statements in MDX files, I'm getting unexpected behavior that causes the imports not to be recognized properly.

### Reproduction

```mdx
import { Component } from './Component'
import { AnotherComponent } from './AnotherComponent'

# My Document

<Component />
<AnotherComponent />
```

When processing this MDX content, the imports don't seem to be parsed correctly. It appears that something is going wrong with how the import keyword is being detected or how the import specifiers are being processed.

### Expected behavior

All import statements should be recognized and processed correctly, allowing the imported components to be used within the MDX document without issues.

### Additional context

This seems to have started happening recently. The imports work in some cases but fail in others, which makes me think there might be an issue with the parsing logic for detecting import/export statements or iterating through import specifiers.

---
Repository: /testbed
