# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX loader where markdown imports are not being detected correctly. It seems like the import detection logic is inverted - files that should be recognized as markdown imports (`.md` and `.mdx` files) are being ignored, while non-markdown files are being treated as markdown imports.

### Reproduction

```js
// This import should be detected as a markdown import but isn't
import Content from './my-doc.mdx';

// Meanwhile, this non-markdown import is incorrectly being treated as markdown
import Component from './MyComponent.js';
```

When processing MDX files with imports, the loader fails to properly identify which imports are actually markdown files. This breaks functionality that depends on distinguishing markdown imports from regular JS/TS imports.

### Expected behavior

The loader should correctly identify imports ending in `.md` or `.mdx` as markdown imports, and treat all other imports as non-markdown imports.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
