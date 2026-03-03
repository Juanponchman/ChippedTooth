import urllib.request, re, os

SOURCE = "https://raw.githubusercontent.com/abusaeeidx/IPTV-Scraper-Zilla/refs/heads/main/PlutoTV-All.m3u"
OUTPUT = "English_Channels_filtered.m3u8"

# Load your channel IDs from the text file
with open("channel_ids.txt") as f:
    wanted = set(line.strip() for line in f if line.strip())

with urllib.request.urlopen(SOURCE) as r:
    lines = r.read().decode("utf-8").splitlines()

out = ["#EXTM3U"]
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("#EXTINF"):
        m = re.search(r'channel-id="([^"]+)"', line)
        if m and m.group(1) in wanted and i + 1 < len(lines):
            out.append(line)
            out.append(lines[i + 1])
        i += 2
    else:
        i += 1

with open(OUTPUT, "w") as f:
    f.write("\n".join(out))

print(f"Done — {(len(out)-1)//2} channels written.")
```

**`channel_ids.txt`** — one channel ID per line (export from your current file):
```
51c75f7bb6f26ba1cd00002f
5417a212ff9fba68282fbf5e
...all 1200 IDs...
