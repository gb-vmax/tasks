# Bug Report

### Describe the bug

I'm encountering an issue with scope initialization in the MDX parser. When parsing MDX content, the scope object doesn't seem to be properly initialized, which causes unexpected behavior during the parsing process.

### Reproduction

```js
// When the parser creates a new scope
const scope = new Scope(flags);

// The scope.flags is undefined instead of the passed flags value
// The scope.functions array contains an empty string instead of being empty
```

This appears to affect how the parser tracks variables and functions within different scopes. The flags parameter isn't being assigned correctly, and the functions array is being initialized with an unexpected value.

### Expected behavior

- `scope.flags` should be set to the `flags` parameter passed to the constructor
- `scope.functions` should be initialized as an empty array `[]`

### System Info

- Package: @mdx-js/mdx@3.0.0
- Environment: Node.js

Has anyone else run into this? It seems like the scope tracking might be broken in the current version.

---
Repository: /testbed
