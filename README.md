tshoot
======

Timpa Device Trouble-shooting
-----------------------------

A vendor with a Timpa experiences a technical problem with the device, then he visits the system’s website and keys in the problem. The devices has elements such as battery, screen, sim, gsm which are stored in the Knowledge base as facts. These elements have specific problems. In the case of “element(battery)” it will be either “flat”,”empty” or “hot”. In the message type by the vendor, the system looks for keywords such as “battery” and “flat”. If found then system will give a solution such as “Connect the machine to the power supply”
The systems assumes that all vendors can write in English language. The correctness of the written query in English is totally ignored. The system only looks for certain keywords and spits out the solution. What happens when those keywords are misspelled by the user/vendor? The system still accepts the query parses and corrects the spelling mistakes then looks for solution.

installing dependencies
------------------------
pip install -r requirements.txt

running
-----------------------
execute ./run.py in your terminal then visit http://localhost:5000
