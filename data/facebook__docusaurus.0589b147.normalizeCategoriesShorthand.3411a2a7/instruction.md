# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category items appearing in reverse order after defining them in the shorthand format. When I use the categories shorthand syntax in my sidebars configuration, the items within each category are displayed in the opposite order from what I specified.

### Reproduction

```js
// sidebars.js
module.exports = {
  mySidebar: {
    'Getting Started': ['intro', 'installation', 'quickstart'],
    'Advanced': ['config', 'deployment', 'troubleshooting']
  }
}
```

Expected order in sidebar:
- Getting Started
  - intro
  - installation
  - quickstart
- Advanced
  - config
  - deployment
  - troubleshooting

Actual order displayed:
- Getting Started
  - quickstart
  - installation
  - intro
- Advanced
  - troubleshooting
  - deployment
  - config

The items are completely reversed from the order I defined them in the configuration.

### Expected behavior

Sidebar items should appear in the same order as they are defined in the shorthand configuration object. The first item in the array should be displayed first, not last.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
