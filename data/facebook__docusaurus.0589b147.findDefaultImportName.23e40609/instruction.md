# Bug Report

### Describe the bug

I'm experiencing an issue with MDX imports in my Docusaurus project. When I try to use default imports in my MDX files, they're not being recognized properly. The imports seem to be ignored and the content doesn't render as expected.

### Reproduction

```mdx
import MyComponent from './MyComponent';

# My Page

<MyComponent />
```

The component doesn't render and appears to be undefined. However, if I use named imports instead, everything works fine:

```mdx
import { MyComponent } from './MyComponent';

# My Page

<MyComponent />
```

### Expected behavior

Default imports should work correctly in MDX files, just like named imports do. The component should be imported and rendered without issues.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently, possibly after an update. Any help would be appreciated!

---
Repository: /testbed
