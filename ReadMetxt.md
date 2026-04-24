# Network Traceroute Visualization Project

Introduction

This project demonstrates how data packets travel across different routers on the Internet using the traceroute command. The program identifies intermediate network hops, extracts their IP addresses, and visualizes the routing path on an interactive world map. This helps in understanding Internet routing and packet forwarding across networks.

Project Overview

The program reads multiple destination websites from a file and performs traceroute for each destination. It extracts the IP addresses of intermediate routers, retrieves their approximate geographical coordinates using an online IP geolocation service, and plots the routing path on a map.

Tools and Technologies Used

1\. Python – Core programming language

2\. traceroute – Network diagnostic tool to discover routing paths

3\. subprocess – To execute traceroute from Python

4\. regex (re) – To extract IP addresses from traceroute output

5\. requests – To fetch IP geolocation data from ipinfo.io

6\. folium – To visualize routing paths on an interactive map

7\. HTML – Used to display the generated map in a browser

How the Project Works

1\. Read destination websites from destination\_list.txt

2\. Run traceroute for each destination

3\. Extract IP addresses of intermediate hops

4\. Obtain latitude and longitude for each IP address

5\. Plot all hops and routing paths on a world map

How to Run the Project

1\. Create a folder named xyz(example).

2\. Then download the files attached (one python file and one text file) and save them in this folder.

3\. Then open Terminal and go to the directory where the folder xyz is saved , then go to folder xyz.

4\. Now type "python filename.py".

5\. Then the code will start running.

6\. At the end , it will show like "Map is saved as traceroute\_map.html".

7\. This map is saved in the xyz folder.

8\. Go to folder xyz and open the map.

9\. Now you can see the markers.

Output Visualization

1\. An interactive HTML world map is generated

2\. Each marker represents a router hop

3\. Lines show the packet routing path

4\. Clicking a marker displays the IP address

Learning Outcomes

1\. Understanding how traceroute works

2\. Practical exposure to network diagnostic tools

3\. Visualization of packet routing paths

4\. Better understanding of Internet routing and network topology

Platform Note

This project is designed for Linux systems.
On Windows, the equivalent command to traceroute is tracert, and the code requires small modifications for compatibility.



