🌐 Traceroute Visualizer

A Python tool that traces network routes to multiple destinations and plots the packet hops on an interactive world map — so you can see where your data actually travels across the internet.

📸 Preview

Each hop along the route is plotted as a marker on a world map, with polylines connecting the hops in order — giving you a visual path of your packets across the globe.

✨ Features

Batch-traces multiple destinations from a simple text file
Runs traceroute and extracts every intermediate IP address
Resolves geolocation for each hop via the ipinfo.io API
Plots hops as interactive markers with IP address popups
Draws polylines connecting hops to show the physical network path
Saves output as a self-contained traceroute_map.html — no server needed


🛠️ Requirements

Python 3.7+
traceroute installed on your system (available on Linux/macOS by default)
Python packages:

  requests
  folium
Install dependencies with:
bashpip install requests folium

🚀 Usage

1. Clone the repository
bashgit clone https://github.com/yourusername/traceroute-visualizer.git
cd traceroute-visualizer
2. Add your target destinations
Edit destination_list.txt and add one domain or IP address per line:
google.com
github.com
cloudflare.com
8.8.8.8
3. Run the script
bashpython visualizer.py
4. Open the map
Open traceroute_map.html in any web browser to explore the interactive map.

📁 Project Structure

traceroute-visualizer/
│
├── visualizer.py          # Main script
├── destination_list.txt   # Your list of target destinations
├── traceroute_map.html    # Generated output map (created on run)
└── README.md

⚙️ How It Works

Reads destination domains/IPs from destination_list.txt
Runs traceroute -m 15 <destination> for each target (max 15 hops)
Parses each line of the traceroute output to extract IP addresses
For each IP, queries the ipinfo.io API to get latitude and longitude
Plots markers and connecting polylines on a Folium world map
Saves the result as traceroute_map.html


⚠️ Notes

traceroute is available natively on Linux and macOS. On Windows, you can use tracert — you'll need to modify the subprocess call in the script accordingly.
Some hops may not appear on the map if the router does not respond to ICMP probes (shown as * * * in traceroute output).
The ipinfo.io free tier allows up to 50,000 requests/month. For heavy use, consider adding your API token.
Geolocation data may not be 100% accurate, especially for private or cloud infrastructure IPs.


🔧 Configuration

You can tweak the following in visualizer.py:
VariableDefaultDescription-m 15 in traceroute args15Maximum number of hops per destinationzoom_start in folium.Map2Initial zoom level of the world map

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements

ipinfo.io for the IP geolocation API
Folium for the interactive map rendering
