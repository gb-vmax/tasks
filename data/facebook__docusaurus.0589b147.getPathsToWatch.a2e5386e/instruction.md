# Bug Report

### Describe the bug

When running the docs plugin in watch mode, file changes are not being detected properly. The development server doesn't seem to pick up changes to markdown files or sidebar configuration files.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Configure multiple include patterns in the plugin options (e.g., `['**/*.md', '**/*.mdx']`)
3. Start the development server
4. Modify a markdown file or the sidebar configuration
5. The changes are not detected and the server doesn't reload

### Expected behavior

The development server should watch all configured file patterns and reload when any matching files are modified. Changes to both content files and sidebar configuration should trigger a reload.

### Additional context

This seems to affect projects with multiple include patterns. The file watcher might not be tracking all the necessary paths correctly.

---
Repository: /testbed
