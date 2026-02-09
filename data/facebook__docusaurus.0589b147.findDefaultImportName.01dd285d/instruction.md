# Bug Report

### Describe the bug

I'm encountering an issue with MDX imports where default imports are not being recognized correctly. When I use a default import statement in my MDX file, it seems like the import name is not being resolved properly, which breaks the component rendering.

### Reproduction

```mdx
---
title: My Page
---

import MyComponent from './MyComponent';

<MyComponent />
```

The component doesn't render and the import appears to be ignored. This worked fine in previous versions but seems to have broken recently.

### Expected behavior

Default imports should be detected and the imported component should render correctly in the MDX file.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
