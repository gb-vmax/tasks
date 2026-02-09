# Bug Report

### Describe the bug

After a recent update, the blog plugin fails to load content properly. The build process crashes with a syntax error when trying to generate blog pages.

### Reproduction

1. Set up a Docusaurus site with the blog plugin enabled
2. Add some blog posts to the blog directory
3. Run the build command
4. The build fails with an error related to the blog plugin's `loadContent` function

### Expected behavior

The blog plugin should successfully load all blog posts and generate the necessary routes without any syntax errors. The build should complete successfully.

### Additional context

This appears to be affecting the blog list pagination and tags functionality. The error occurs during the content loading phase before any pages are generated.

---
Repository: /testbed
