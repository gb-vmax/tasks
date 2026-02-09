# Bug Report

Title: Sidebar normalization broken - passing wrong arguments

### Describe the bug
I'm experiencing an issue with sidebar normalization in the docs plugin. When I have multiple sidebars configured, the normalization process seems to be passing incorrect data, which causes the sidebars to not render properly or throw errors.

### Reproduction
```js
// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['intro', 'basics'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API',
      items: ['api-overview'],
    },
  ],
};
```

When the plugin tries to normalize these sidebars, it appears to be processing them incorrectly. Instead of normalizing each individual sidebar array, it seems like the entire sidebars object is being passed where a single sidebar should be.

### Expected behavior
Each sidebar should be normalized independently with its correct configuration and identifier. The normalization should process `tutorialSidebar` and `apiSidebar` separately with their respective items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
