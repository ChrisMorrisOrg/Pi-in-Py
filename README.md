# Pi in Py

By [Chris Morris](http://chrismorris.org).

A simple little Python application to approximate pi using various methods.

Running the App
---------------
Simply run in IDLE or open Terminal and run "python pi.py" inside the directory where pi.py is stored.
Requires Python 3.x.

###Please note that:
- This app can slow down your computer considerably as well as drain your battery. Please save all work prior to running the application, and always start with a small number of iterations (try 100).
- You can exit the app by using ctrl+C at any time.

Background
----------
This app was simply created as a way for me to visualise how different methods work when approximating pi, and to also calculate the convergence times. It was also a good excuse to practice some Python!

Please feel free to fork and add other methods for calculating pi.

Version History
---------------
### v0.3 (2013-Jan-04)
- Allows users to approximate pi using Euler's formula.
- Methods are now timed.
- Forces Python 3.x use.

### v0.2 (2013-Jan-03)
- Fixed the message loop stating the ordering of addition and subtraction in the Divide-Subtract-Divide-Add algorithm (algorithm remains the same).
- Allows users to approximate pi using Madheva's formula iteratively.
- Added menu and basic UI.
- Added overflow handler.

### v0.1 (2013-Jan-02)
- Allows users to approximate pi by calculating 4*(1 - 1/3 + 1/5 - 1/7 +...) iteratively.
