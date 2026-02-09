# Bug Report

### Describe the bug

I'm encountering an issue with syntax extension merging in the MDX parser. When multiple syntax extensions are combined, the hooks are not being properly registered and the parser fails to recognize certain syntax constructs.

### Reproduction

```js
const extension1 = {
  flow: {
    42: { tokenize: flowTokenize1 }
  }
}

const extension2 = {
  flow: {
    42: { tokenize: flowTokenize2 }
  }
}

// Merge extensions
const combined = syntaxExtension({}, extension1)
syntaxExtension(combined, extension2)

// The combined extension doesn't contain the expected constructs
// Parser fails to recognize syntax that should be supported
```

### Expected behavior

When merging syntax extensions, all hooks and constructs from both extensions should be properly combined and available in the resulting configuration. The parser should recognize all registered syntax constructs.

### Additional context

This seems to affect the ability to use multiple MDX plugins that register syntax extensions for the same hook types. The extensions appear to overwrite each other instead of merging properly.

---
Repository: /testbed
