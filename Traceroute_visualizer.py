import subprocess
import re
import requests
import folium

f = open("destination_list.txt", "r")
lines = f.readlines()
f.close()

points = []

for d in lines:
    d = d.strip()
    if d == "":
        continue

    print("Tracing:", d)

    p = subprocess.Popen(
        ["traceroute", "-m", "15", d],
        stdout=subprocess.PIPE,
        text=True
    )

    for l in p.stdout:
        m = re.search(r"\((\d+\.\d+\.\d+\.\d+)\)", l)
        if m:
            ip = m.group(1)
            print("IP:", ip)

            try:
                res = requests.get("https://ipinfo.io/" + ip + "/json")
                info = res.json()

                if "loc" in info:
                    loc = info["loc"].split(",")
                    points.append((ip, float(loc[0]), float(loc[1])))
            except:
                pass

mp = folium.Map(location=[20, 0], zoom_start=2)

prev = None
for p in points:
    ip = p[0]
    lat = p[1]
    lon = p[2]

    folium.Marker(
        [lat, lon],
        popup=ip
    ).add_to(mp)

    if prev:
        folium.PolyLine(
            [[prev[1], prev[2]], [lat, lon]]
        ).add_to(mp)

    prev = p

mp.save("traceroute_map.html")
print("Map saved as traceroute_map.html")
