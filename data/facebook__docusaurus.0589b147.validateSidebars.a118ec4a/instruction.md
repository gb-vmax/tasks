# Bug Report

### Describe the bug

I'm encountering an issue with sidebar validation in the docs plugin. When I try to build my documentation site, it fails with a cryptic error about sidebar items not being validated properly.

### Reproduction

```js
// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['hello', 'world'],
    },
  ],
  apiSidebar: [
    {
      type: 'doc',
      id: 'api-intro',
    },
  ],
};
```

When building the docs with the above sidebar configuration, I get an error like:

```
TypeError: sidebar.map is not a function
```

### Expected behavior

The sidebars should be validated correctly and the build should succeed without errors. This configuration worked fine in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
