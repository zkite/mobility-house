### General

To build an application which generates simulated PV (photovoltaic) power values (in kW).

### Requirements
+ Meter: should produce messages to the broker with random but continuous values from 0 to 9000 Watts. 
  This is to mock a regular home power consumption.
+ PV simulator: It must listen to the broker for the meter values, generate a simulated PV power value 
  and add this value to the meter value and output the result.
+ The result should be saved in a file with a timestamp, meter power value, 
  PV power value and the sum of the powers (meter + PV). The period of a day with samples every couple of seconds would be enough.


### Run Simulation
---
Please make sure you have installed Docker latest version.

To run the app, do the following commands:
- pull fresh images from the repo and build
>docker-compose build --no-cache

- run application
>docker-compose up

Please check generated files in the app/files directory.

### Testing
Please make sure your PYTHONPATH env is set up properly.

To run the tests, do the following command:
 >python -m pytest

### Notes
+ As the application totaly runs under the docker I've decided to mount app/files directory to the docker PV container, 
  so you can find generated files both in the PV container app directory and on your local machine.


