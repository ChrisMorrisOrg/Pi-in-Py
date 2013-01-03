# Pi in Py

By [Chris Morris](http://chrismorris.org).

A simple little Python application to calculate pi to as many digits as possible using various methods.

Running the App
---------------
Simply run in IDLE or open Terminal and run "python pi.py" inside the directory where pi.py is stored.
Requires Python 3.x.

###Please note that:
- This app can slow down your computer considerably as well as drain your battery. Please save all work prior to running the application, and then start with a small number of iterations.
- You can exit the app by using ctrl+C at any time.

###Tips:
- 10,000 iterations should result in roughly 4-digit accuracy.
- 100,000 iterations should result in roughly 5-digit accuracy.

Background
----------
This app was simply created as a way for me to visualise how different methods work on approximating pi, and to also calculate the convergence times. It was also a good excuse to practice some Python!

Please feel free to fork or add other methods.

Version History
---------------
### v0.2 (2013-01-03)
- Allows users to approximate pi using the Madheva method iteratively.
- Added menu and basic UI
- Added overflow handler

### v0.1 (2013-01-02)
- Allows users to approximate pi by calculating 4*(1 - 1/3 + 1/5 - 1/7 +...) iteratively.
