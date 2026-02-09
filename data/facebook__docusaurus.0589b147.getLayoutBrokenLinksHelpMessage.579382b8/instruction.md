# Bug Report

### Broken links help message not showing when expected

I'm experiencing an issue where the broken links detection feature isn't showing the helpful layout message when it should. 

When I have multiple pages with the same broken link (like a navbar or footer link that appears on every page), I expect to see a message suggesting that the broken link might be in the layout/theme configuration. However, this message doesn't appear even when the broken link is present on many pages.

### To Reproduce

1. Add a broken link to your navbar or footer (something that appears on multiple pages)
2. Build the site with broken link detection enabled
3. The broken link is reported, but the helpful message about checking theme configuration doesn't show up

For example, if I have a broken link in my navbar that appears on 10+ pages, I would expect to see:

```
It looks like some of the broken links we found appear in many pages of your site.
Maybe those broken links appear on all pages through your site layout?
We recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
```

But this message is missing from the output.

### Expected Behavior

The broken links checker should detect when the same broken link appears frequently across multiple pages and provide the helpful message about checking the theme/layout configuration.

This is especially useful for broken links that are in the navbar, footer, or other layout components that appear on every page.

---
Repository: /testbed
