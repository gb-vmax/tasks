# Bug Report

### Describe the bug

I'm encountering a runtime error when validating sidebars configuration. The validation function crashes with a `TypeError` stating that `sidebar.forEach is not a function`.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['intro', 'basics'],
    },
  ],
  apiSidebar: [
    {
      type: 'doc',
      id: 'api-reference',
    },
  ],
};

// Calling validateSidebars with this configuration throws an error
validateSidebars(sidebars);
```

### Expected behavior

The sidebar validation should complete successfully without throwing any errors when provided with a valid sidebar configuration object.

### Error message

```
TypeError: sidebar.forEach is not a function
```

It seems like the validation is trying to iterate over something that isn't an array. This is blocking my ability to use multiple sidebars in my Docusaurus configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
