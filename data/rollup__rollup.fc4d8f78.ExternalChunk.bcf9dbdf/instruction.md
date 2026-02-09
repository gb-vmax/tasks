# Bug Report

### Issue with external module path resolution

I'm experiencing incorrect path generation for external modules in my build output. The paths to external dependencies are being generated incorrectly, which breaks imports in the bundled code.

### Reproduction

When I have an external module configured and build my project, the generated import paths are wrong. 

Setup:
```js
{
  external: ['some-external-lib'],
  output: {
    format: 'es'
  }
}
```

The generated bundle produces import paths that don't correctly resolve to the external module. For example, if my source file is at `src/components/MyComponent.js` and imports an external library, the relative path calculation seems inverted.

### Expected behavior

External module imports should generate correct relative paths (or absolute paths when appropriate) that properly resolve to the external dependency from the importing file's location.

### Additional context

This seems to affect how the bundler calculates paths between the importer and the external module. The path resolution logic might have the arguments in the wrong order or the condition for when to normalize paths might be inverted.

---
Repository: /testbed
