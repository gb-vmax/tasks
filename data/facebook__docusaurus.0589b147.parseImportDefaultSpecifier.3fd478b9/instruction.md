# Bug Report

### Describe the bug

I'm experiencing an issue with import statements in MDX files. When using default imports, they seem to be parsed incorrectly, which is causing problems with how the imports are being handled.

### Reproduction

```js
import MyComponent from './MyComponent'

// The default import is not being recognized correctly
// This causes issues when trying to use MyComponent in the MDX file
```

When I have a simple default import statement in my MDX file, the parser appears to be treating it differently than expected. The import statement itself doesn't throw an error during parsing, but the imported component behaves unexpectedly.

### Expected behavior

Default imports should be parsed as `ImportDefaultSpecifier` nodes and treated with the appropriate binding type. The imported component should be usable normally within the MDX content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

Has anyone else run into this? It seems like the parser might be misidentifying the import type.

---
Repository: /testbed
