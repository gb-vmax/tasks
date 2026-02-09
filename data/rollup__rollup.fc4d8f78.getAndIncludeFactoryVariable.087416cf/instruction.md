# Bug Report

### Describe the bug

I'm experiencing an issue with JSX factory imports when using a custom `importSource` with a nested factory name (e.g., `React.createElement`). The import statement seems to be importing the wrong specifier.

### Reproduction

When configuring JSX with:
```js
{
  jsx: {
    factory: 'React.createElement',
    importSource: 'react'
  }
}
```

The bundler appears to be importing the nested name (`React`) as the default import instead of importing `createElement` from the named export. This causes the generated code to reference the wrong import.

### Expected behavior

When using a nested factory name like `React.createElement` with an `importSource`, it should:
1. Import the base name (`React`) from the import source
2. Access the nested property (`createElement`) on that import

Instead, it seems to be doing the opposite - treating the nested name as if it should be the default import.

### Additional context

This affects JSX transformation when using custom pragma with import sources. The issue manifests when the factory function is specified as a nested property access rather than a simple identifier.

---
Repository: /testbed
