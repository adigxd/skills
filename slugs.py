import re

pth_i = "slugs.md"
pth_o = "preview.md"

rgx = re.compile(r"^\| `.+?` \| `(.+?)` \|")

lin_arr = []

with open(pth_i, encoding="utf-8") as f:
    for lin in f:
        rgx_yes = rgx.match(lin.strip())

        if rgx_yes:
            slug = rgx_yes.group(1)
            lin_arr.append(
                f"[![{slug}](https://img.shields.io/badge/ABC-C0E8E0?style=for-the-badge&logo={slug})](https://github.com/adigxd/r)\n"
            )

with open(pth_o, "w", encoding="utf-8") as f:
    f.writelines(lin_arr)
