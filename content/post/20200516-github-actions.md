+++
title = "DNS Records for GitHub Pages"
description = ""
tags = [
    "GitHub",
    "GitHub Pages",
    "DNS",
]
date = "2020-05-16"
categories = [
    "Development",
]
+++

Every once in a while I need to modify my custom domain's DNS records to work with GitHub pages, and every time it's a struggle to get it right. Here I document my currently-working setup.

I followed the recommended setup[<sup>1</sup>][1] by configuring **www** as my **Custom Domain**, also configuring my apex domain, and letting GitHub Pages "automatically create redirects between the domains". Specifically for this website, I told GitHub that my **Custom Domain** is www.charlesjlee.com and I setup the DNS records for [charlesjlee.com](http://charlesjlee.com). This involved making changes in three places: DNS records, repo config, site config.

### DNS records
My DNS provider is GoDaddy. I added the below five entries to my DNS Records table. The first four **A** records map the current domain ([charlesjlee.com](http://charlesjlee.com)) to the IP addresses for GitHub Pages. The last **CNAME** record maps the **www** subdomain (www.charlesjlee.com) to the current domain ([charlesjlee.com](http://charlesjlee.com)) so that the **www** subdomain (www.charlesjlee.com) also points to GitHub Pages' IP addresses.

{{<pure_table
    "Type|Name|Value|TTL"
    "A|@|185.199.108.153|1 hour"
    "A|@|185.199.109.153|1 hour"
    "A|@|185.199.110.153|1 hour"
    "A|@|185.199.111.153|1 hour"
    "CNAME|www|@|1 hour"
>}}

After these records are added, you can confirm that DNS is resolving correctly by using `nslookup` for Windows or `dig` for Linux. While DNS changes can take a long time (24-72 hours) to propagate worldwide, in my experience, I saw changes appear within minutes.
```PowerShell
PS C:\Hugo\charlesjlee-website> nslookup charlesjlee.com                                               Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    charlesjlee.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153

PS C:\Hugo\charlesjlee-website> nslookup www.charlesjlee.com                                           Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    charlesjlee.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
Aliases:  www.charlesjlee.com
```

### Repo config
On GitHub, navigate to the **Settings** tab for your repo and scroll all the way to the bottom to see the **GitHub Pages** section. Here, you want to:
1. Set **Source** to the correct branch
2. Set **Custom domain** as the **www** subdomain
3. Optionally enable HTTPS

If the DNS records and repo config are correct, you will see a green bar, otherwise, you will see a yellow bar.

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20200516-github-pages-dns-settings.png|Configuring GitHub Pages" 
>}}

### Site config
Finally, you'll want to add or update the `CNAME` file in your `gh-pages` branch (or whichever branch you specified above) to be the **www** subdomain (www.charlesjlee.com).

If you're generating the CNAME file, e.g. by using GitHub Actions, don't forget to update your workflow script.

If you enabled HTTPS earlier, make sure your files internally refer to HTTPS or the apex URL to avoid serving mixed content. If you're using Hugo, this could mean updating `BaseURL` in `config.toml`.

## References
1. https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site

[1]: https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site
