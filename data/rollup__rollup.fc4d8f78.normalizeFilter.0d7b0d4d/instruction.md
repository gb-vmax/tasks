# Bug Report

### Describe the bug

When passing a string or RegExp directly to `createFilter()`, it's being treated as an exclusion pattern instead of an inclusion pattern. This is the opposite of what the documentation states and what users would expect.

### Reproduction

```js
import { createFilter } from 'rollup-pluginutils';

// This should include only .js files, but instead it excludes them
const filter = createFilter('*.js');

console.log(filter('test.js'));  // Expected: true, Actual: false
console.log(filter('test.css')); // Expected: false, Actual: true
```

Similarly with RegExp:

```js
const filter = createFilter(/\.ts$/);

console.log(filter('index.ts'));  // Expected: true, Actual: false
console.log(filter('index.js'));  // Expected: false, Actual: true
```

Also affects the object form:

```js
const filter = createFilter({
  include: ['src/**'],
  exclude: ['node_modules/**']
});

// The include and exclude patterns appear to be swapped
console.log(filter('src/main.js'));           // Expected: true, Actual: false
console.log(filter('node_modules/lib.js'));   // Expected: false, Actual: true
```

### Expected behavior

- String/RegExp filters should be treated as inclusion patterns
- When using the object form, `include` should include files and `exclude` should exclude files

### System Info

- rollup-pluginutils version: latest
- Node version: 18.x

---
Repository: /testbed
