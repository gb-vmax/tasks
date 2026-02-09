# Bug Report

### Describe the bug

I'm encountering an issue where the AST (Abstract Syntax Tree) returned by transform plugins is being lost during the transformation process. When a plugin returns an object with `code` and `ast` properties, the `ast` is no longer being preserved for subsequent processing.

### Reproduction

```js
// Plugin that returns both code and ast
const plugin = {
  name: 'test-plugin',
  transform(code, id) {
    return {
      code: transformedCode,
      ast: parsedAst,  // This gets lost
      map: sourceMap
    };
  }
};

// The ast is not available after transformation
// even though the plugin returned it
```

### Expected behavior

When a transform plugin returns an object containing an `ast` property along with `code`, the AST should be preserved and made available for downstream processing. This is important for plugins that need to access or modify the AST without re-parsing the code.

### Additional context

This seems to have started happening recently. The AST was previously being extracted from the result object but now it's not being assigned anywhere, causing it to be lost even though the plugin is returning it correctly.

---
Repository: /testbed
