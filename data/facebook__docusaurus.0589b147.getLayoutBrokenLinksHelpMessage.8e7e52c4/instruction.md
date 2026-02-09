# Bug Report

### Describe the bug

The broken links detection message is displaying incorrectly with truncated text. When there are frequent broken links that appear across multiple pages, the help message that suggests checking the theme layout has missing characters at the beginning of several lines.

### Reproduction

1. Create a Docusaurus site with broken links that appear frequently across multiple pages (e.g., in navbar or footer)
2. Run the build process
3. Observe the broken links error message

The output shows:
```
looks like some of the broken links we found appear in many pages of your site.
ybe those broken links appear on all pages through your site layout?
recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
equent broken links are linking to:...
```

### Expected behavior

The message should display properly formatted text:
```
It looks like some of the broken links we found appear in many pages of your site.
Maybe those broken links appear on all pages through your site layout?
We recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
Frequent broken links are linking to:...
```

The help message is missing the first few characters of each line ("It", "Ma", "We", "Fr"), making it harder to read and understand the guidance being provided.

---
Repository: /testbed
