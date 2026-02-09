# Bug Report

### Describe the bug

After a recent update, I'm seeing issues with property enumeration on exported objects. Properties that should be enumerable are no longer showing up when iterating over objects or using methods like `Object.keys()`.

### Reproduction

```js
// When importing from the affected module
import { someExport } from 'rehype-stringify';

// These no longer work as expected:
console.log(Object.keys(someExport)); // Returns empty array or missing properties
for (let key in someExport) {
  console.log(key); // Doesn't iterate over properties that should be there
}

// Properties exist but aren't enumerable
console.log(someExport.propertyName); // Works fine
console.log(Object.getOwnPropertyDescriptor(someExport, 'propertyName').enumerable); // false
```

### Expected behavior

Exported properties should be enumerable by default, allowing them to be discovered through `Object.keys()`, `for...in` loops, and other enumeration methods. This is how it worked in the previous version.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

This seems to have broken after the latest changes. Any code that relies on enumerating exported properties is now failing.

---
Repository: /testbed
