# Bug Report

### Describe the bug

I'm experiencing an issue where `attentionMarkers` seems to be getting modified unexpectedly when accessed multiple times. The array appears to lose elements on subsequent accesses, which is causing inconsistent behavior in my markdown parsing.

### Reproduction

```js
// First access
const markers1 = constructs_exports.attentionMarkers;
console.log(markers1.length); // e.g., 2

// Second access
const markers2 = constructs_exports.attentionMarkers;
console.log(markers2.length); // e.g., 1 (should be 2)

// Third access
const markers3 = constructs_exports.attentionMarkers;
console.log(markers3.length); // e.g., 0 (should be 2)
```

Each time I access `attentionMarkers`, the array gets shorter. It looks like the original array is being mutated instead of returning a fresh copy each time.

### Expected behavior

The `attentionMarkers` export should return the same consistent data on every access. The underlying array should not be modified by simply reading the export.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
