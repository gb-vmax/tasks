# Bug Report

### Describe the bug

When using the docs plugin with a custom sidebar file, hot reload isn't working properly. Changes to the sidebar configuration file don't trigger a rebuild/reload of the documentation site during development. I have to manually restart the dev server every time I modify the sidebar.

### Reproduction

1. Set up a Docusaurus site with the docs plugin
2. Configure a custom sidebar file in your plugin options
3. Start the dev server
4. Make changes to the sidebar configuration file
5. Notice that the changes don't appear - the site doesn't reload

### Expected behavior

The dev server should detect changes to the sidebar file and automatically reload the documentation, similar to how it reloads when markdown files are modified.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
