# Bug Report

### Describe the bug

I'm experiencing an issue with footnote IDs in blog posts where the footnote references and definitions are getting out of sync. When I use footnotes in my markdown files, the links between the footnote markers in the text and their corresponding definitions at the bottom of the page are broken.

### Reproduction

Create a blog post with footnotes:

```markdown
Here is some text with a footnote[^1].

And another footnote[^2].

[^1]: First footnote definition
[^2]: Second footnote definition
```

When the page renders, clicking on the footnote reference `[^1]` in the text doesn't navigate to the correct footnote definition, or the link is completely broken.

### Expected behavior

Footnote references should correctly link to their corresponding footnote definitions. The IDs for both the reference and definition should match so that clicking a footnote marker takes you to the right definition at the bottom of the page.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
