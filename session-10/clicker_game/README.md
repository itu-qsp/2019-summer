# A Simple Game written in Brython

Find the IP address of your computer either with `ifconfig` (MacOS/Linux) or `ipconfig` on Windows.


Alternatively, you can run the following small Python program to find the IP address of your computer:

```python
import socket


host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print(f"My computer's IP address: {ip_address}")
```



Now, start an HTTP server in this directory:

```bash
python -m http.server
```


Point a browser, either from your mobile phone or from another computer to http://<ip_address>:8000 and start playing.

To be able to connect your browser to the given IP address, all involved devices, i.e., the computer serving the game, and all the clients have to be on the same network. At ITU this is for example ITU++.