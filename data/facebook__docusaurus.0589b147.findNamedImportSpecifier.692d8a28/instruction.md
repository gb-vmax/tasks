# Bug Report

### Describe the bug

I'm having an issue with named imports in MDX files. When trying to import a specific named export from a module, it seems like the import is not being recognized correctly. The code appears to be looking for default imports instead of named imports.

### Reproduction

```js
import { MyComponent } from './components';

// MyComponent is not found/recognized
<MyComponent />
```

The import statement should work but it seems like the parser is checking for default imports when it should be checking for named imports.

### Expected behavior

Named imports like `import { MyComponent }` should be properly detected and processed. The component should be available for use in the MDX file.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
