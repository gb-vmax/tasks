# Bug Report

### Describe the bug

The plugin is not watching the correct file paths in development mode. After making changes to documentation files, the dev server doesn't pick up the changes and hot reload isn't working properly.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Configure `include` patterns in the plugin options (e.g., `['**/*.md', '**/*.mdx']`)
3. Start the dev server
4. Edit a markdown file in your docs directory
5. Changes are not detected and the browser doesn't reload

### Expected behavior

The dev server should watch all documentation files matching the include patterns and automatically reload when they change. File changes should be detected regardless of the directory structure.

### Additional context

This seems to affect the file watching mechanism. The sidebar configuration file also doesn't seem to be watched correctly - it appears at the end of the watch list instead of at the beginning where it should be prioritized.

---
Repository: /testbed
