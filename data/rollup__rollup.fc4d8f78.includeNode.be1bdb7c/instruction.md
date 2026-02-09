# Bug Report

### Describe the bug

I'm experiencing an issue with `import.meta` properties not being handled correctly. When I try to access custom properties on `import.meta`, they aren't being processed as expected and the build seems to be ignoring them entirely.

### Reproduction

```js
// In my module code
console.log(import.meta.url);
console.log(import.meta.custom);
```

When bundling this code, the `import.meta` references don't seem to be getting tracked or transformed properly. The context doesn't appear to be receiving the meta property information.

### Expected behavior

The bundler should detect and process `import.meta` usage, allowing plugins to handle these meta properties appropriately. Custom properties on `import.meta` should be recognized and made available to the plugin system.

### Additional context

This seems to have started happening recently. Previously, `import.meta` was being detected and handled correctly during the bundling process. Now it's as if the meta property detection logic isn't triggering at all.

---
Repository: /testbed
