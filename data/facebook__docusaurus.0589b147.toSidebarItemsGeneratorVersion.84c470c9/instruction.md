# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar item generation where the version information passed to the generator function appears to be incorrect. The generator is receiving properties that don't match what's documented or expected.

### Reproduction

When using a custom sidebar items generator function, the `version` parameter doesn't contain the expected properties:

```js
module.exports = {
  docs: {
    async sidebarItemsGenerator({defaultSidebarItemsGenerator, version, ...args}) {
      console.log(version);
      // Expected: { versionName: '1.0.0', contentPath: '/path/to/docs' }
      // Actual: { version: '1.0.0', contentPathDir: '/path/to/docs' }
      
      // This breaks existing code that relies on version.versionName
      const items = await defaultSidebarItemsGenerator(args);
      return items;
    }
  }
};
```

### Expected behavior

The `version` object passed to `sidebarItemsGenerator` should contain:
- `versionName`: The name/number of the version
- `contentPath`: The path to the version's content directory

This is what the documentation indicates and what worked in previous versions.

### Additional context

This seems to have changed recently and is breaking custom sidebar generators that depend on these property names. Any code accessing `version.versionName` or `version.contentPath` will fail.

---
Repository: /testbed
