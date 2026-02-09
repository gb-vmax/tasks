# Bug Report

### Describe the bug

I'm getting an error when trying to start my Docusaurus site even though I have a valid config file. The error message says "No config file found" and then immediately crashes, but my `docusaurus.config.js` file definitely exists in the site directory.

### Reproduction

1. Create a new Docusaurus site with a standard `docusaurus.config.js` file
2. Try to run the site (build or start)
3. Get error: "No config file found."

This is really strange because the config file is right there in the root directory. I haven't changed anything unusual in my setup.

### Expected behavior

The site should start normally and detect the config file. It worked fine before, but now it's not finding the configuration even when it exists.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

Has anyone else experienced this? Any help would be appreciated!

---
Repository: /testbed
