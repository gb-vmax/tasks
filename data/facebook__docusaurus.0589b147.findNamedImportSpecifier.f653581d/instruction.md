# Bug Report

### Describe the bug

I'm experiencing an issue with named imports in MDX files. When trying to import specific named exports from a module, the imports are not being recognized correctly and the code fails to work as expected.

### Reproduction

```js
import { SomeComponent } from './components';

// SomeComponent is undefined or not found
<SomeComponent />
```

The named import `SomeComponent` doesn't seem to be detected properly. It works fine with default imports, but breaks when using named imports with curly braces.

### Expected behavior

Named imports should be correctly identified and made available in the MDX file. The component should render without issues.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
