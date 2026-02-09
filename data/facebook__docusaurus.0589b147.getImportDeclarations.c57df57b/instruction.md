# Bug Report

### Describe the bug

I'm experiencing an issue with MDX imports in Docusaurus where import statements are not being recognized or processed correctly. It seems like the import declarations are being filtered out incorrectly, causing imports to not work as expected.

### Reproduction

When I have an MDX file with multiple imports like:

```mdx
import Component1 from './Component1';
import Component2 from './Component2';
import Component3 from './Component3';

# My Page

<Component1 />
<Component2 />
<Component3 />
```

The components are not being imported properly. It appears that the first import is being skipped and the rest are not being treated as import declarations at all.

### Expected behavior

All import statements should be correctly identified and processed so that imported components can be used within the MDX content.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The imports were working fine before, but now they're being filtered out or skipped somehow.

---
Repository: /testbed
