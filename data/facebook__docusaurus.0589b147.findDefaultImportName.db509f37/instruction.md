# Bug Report

### Describe the bug

I'm experiencing an issue with MDX imports where default imports are not being recognized correctly. When I use a default import statement in my MDX file, the imported component/module name is not being resolved properly.

### Reproduction

In an MDX file, when using a default import like:

```mdx
import MyComponent from './MyComponent';

# My Page

<MyComponent />
```

The default import name is not being detected, causing the component to not render or be recognized in the table of contents processing.

### Expected behavior

Default imports should be properly identified and their names extracted so they can be used throughout the MDX document. The import declaration should recognize `ImportDefaultSpecifier` types and return the correct local name.

### System Info
- Docusaurus version: latest
- MDX loader: docusaurus-mdx-loader

This seems to have started recently and is affecting how imports are processed in the remark TOC plugin. Any help would be appreciated!

---
Repository: /testbed
