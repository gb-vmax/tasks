# Bug Report

### Describe the bug

The sidebar normalization is returning an array instead of an object, which breaks the expected structure of normalized sidebars. This causes issues when trying to access sidebars by their ID keys.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['hello'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API',
      items: ['intro'],
    },
  ],
};

const normalized = normalizeSidebars(sidebars);

// Expected: normalized.tutorialSidebar should exist
// Actual: normalized is an array, not an object with keys
console.log(normalized.tutorialSidebar); // undefined
```

### Expected behavior

`normalizeSidebars()` should return an object with the same keys as the input, where each sidebar is normalized. The function should preserve the object structure so sidebars can be accessed by their ID.

Expected output structure:
```js
{
  tutorialSidebar: [...normalized items...],
  apiSidebar: [...normalized items...]
}
```

Actual output is an array instead of an object.

---
Repository: /testbed
