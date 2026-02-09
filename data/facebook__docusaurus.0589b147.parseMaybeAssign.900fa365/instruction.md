# Bug Report

### Describe the bug

I'm experiencing a critical issue with the MDX parser after a recent update. When trying to parse MDX files, the parser completely fails and produces garbled output instead of properly parsing assignment expressions.

### Reproduction

```js
// Any MDX file with assignment expressions fails to parse
const mdxContent = `
export const value = 42;

# Hello World
`;

compile(mdxContent); // Parser crashes or produces invalid output
```

The issue appears to affect all MDX parsing operations, particularly when the content includes:
- Variable assignments
- Destructuring expressions  
- Arrow functions
- Any expression that would normally be handled by `parseMaybeAssign`

### Expected behavior

The MDX compiler should successfully parse assignment expressions and other JavaScript expressions within MDX files without errors. Previously this worked fine.

### Additional context

This seems to have broken after the latest changes to the vendor files. The parser is completely unable to handle basic JavaScript syntax that should be valid in MDX files. This is blocking our entire MDX-based documentation system.

---
Repository: /testbed
