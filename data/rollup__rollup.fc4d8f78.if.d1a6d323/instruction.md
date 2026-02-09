# Bug Report

### Describe the bug

I'm encountering an issue with dynamic imports where modules that should be treated as dynamic entries are being incorrectly excluded from the bundle. It seems like the logic for detecting which dynamically imported modules need to be added as entry points is inverted or broken.

### Reproduction

When I have a setup like this:

```js
// main.js (entry point)
import './moduleA.js';

// moduleA.js
const dynamicModule = await import('./dynamic.js');

// dynamic.js
export default { foo: 'bar' };
```

The `dynamic.js` module should be identified as a dynamic entry, but it's not being included in the output as expected. The module graph analysis seems to be skipping modules that have dynamic importers.

### Expected behavior

Dynamically imported modules that have at least one dynamic importer should be correctly identified and added to the set of dynamic entry modules. The bundler should properly handle these modules and include them in the output.

### Additional context

This appears to be related to how the module graph is being analyzed when determining which modules should be treated as dynamic entries. The condition for adding modules to the dynamic entries set might not be working as intended.

---
Repository: /testbed
