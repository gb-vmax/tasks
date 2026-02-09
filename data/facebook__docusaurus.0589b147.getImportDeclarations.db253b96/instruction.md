# Bug Report

### Describe the bug

The MDX loader is skipping the first import statement in files. When processing MDX files with multiple imports, the first import declaration is not being detected/processed correctly, which can cause issues with component resolution and module loading.

### Reproduction

Create an MDX file with multiple imports:

```mdx
import ComponentA from './ComponentA';
import ComponentB from './ComponentB';
import ComponentC from './ComponentC';

# My Document

<ComponentA />
<ComponentB />
<ComponentC />
```

When the file is processed, `ComponentA` import is missing from the import declarations list, while `ComponentB` and `ComponentC` are correctly identified.

### Expected behavior

All import declarations should be detected and processed, including the first one in the file. The import for `ComponentA` should be included in the list of imports just like the others.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
