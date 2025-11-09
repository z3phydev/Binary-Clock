## Binary Clock
# What is it?
A binary clock is a digital clock that displays the time using binary numbers instead of traditional digits. Each column represents a digit of time, so the first column is the Tens Dight of the hours, and every LED vertically is a number in binary format.
# Why did I make it?
I was originally inspired by seeing a software demo by the YouTube channel, Figuring Things Out. I wanted to try creating something similar but as a physical desk clock. The result is a clock that most people can't read but find cool. I like how the exposed PCB give it even more of that digital vibe.


## PCB
<img width="1560" height="517" alt="image" src="https://github.com/user-attachments/assets/0e845a50-9630-47dc-960d-207c3b23bae1" />

## PCB and Stand Render
Sadly not all the parts exported, might have to add them in

<img width="952" height="721" alt="image" src="https://github.com/user-attachments/assets/574b28f3-5807-4069-9f5f-298ebd0f504c" />

## Schematic

<img width="4960" height="3507" alt="image" src="https://github.com/user-attachments/assets/a71aa076-6d55-4d71-8b1e-9b5ad709bb66" />


## BOM

|Reference                                                                      |Qty|Value/Description|MFR               |MFR No.                |Mouser No.          |Datasheet                                                                    |Unit Price GBP|Total Price GBP|Note                                                  |FIELD11 |FIELD12               |FIELD13        |
|-------------------------------------------------------------------------------|---|-----------------|------------------|-----------------------|--------------------|-----------------------------------------------------------------------------|--------------|---------------|------------------------------------------------------|--------|----------------------|---------------|
|A1                                                                             |1  |Raspberry Pi Pico|Raspberry Pi      |SC0915                 |358-SC0915          |https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf                   |4.8           |4.8            |If you want the headers you will need to buy elsewhere|        |                      |               |
|D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20         |20 |RED LED          |Cree LED          |C5SMF-RJF-CT0W0BB2     |941-C5SMFRJFCT0W0BB2|~                                                                            |0.116         |2.32           |                                                      |        |                      |               |
|J1                                                                             |1  |USB C            |GCT               |USB4085-GF-A           |640-USB4085-GF-A    |https://www.usb.org/sites/default/files/documents/usb_type-c.zip             |0.643         |0.643          |                                                      |        |                      |               |
|Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18,Q19,Q20         |20 |NPN Transistor   |onsemi / Fairchild|BC547BBU               |512-BC547BBU        |https://ngspice.sourceforge.io/docs/ngspice-html-manual/manual.xhtml#cha_BJTs|0.098         |1.96           |                                                      |        |                      |               |
|R1,R2                                                                          |2  |5.1kOhm Resistor |KOA Speer         |MF1/4DCT52R5101F       |660-MF1/4DCT52R5101F|~                                                                            |0.085         |0.17           |                                                      |        |                      |               |
|R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22       |20 |154Ohm Resistor  |Vishay / Beyschlag|MBA02040C1540FRP00     |594-MBA02040C1540FRP|~                                                                            |0.057         |1.14           |                                                      |        |                      |               |
|R23,R24,R25,R26,R27,R28,R29,R30,R31,R32,R33,R34,R35,R36,R37,R38,R39,R40,R41,R42|20 |1.18kOhm Resistor|YAGEO             |MFR-25FRF52-1K18       |603-MFR-25FRF52-1K18|~                                                                            |0.029         |0.58           |                                                      |        |                      |               |
|SW1                                                                            |1  |Button           |Same Sky          |TS02-66-70-BK-260-LCR-D|179-TS026670BK260LCR|~                                                                            |0.73          |0.7            |                                                      |        |                      |               |
|U1                                                                             |1  |DS3231 RTC Module|WINGONEER         |ASIN : B01H5NAFUY      |                    |http://datasheets.maximintegrated.com/en/ds/DS3231.pdf                       |3.99          |3.99           |Amazon link : https://amzn.eu/d/fGpd2tB               |        |                      |               |
|                                                                               |   |                 |                  |                       |                    |                                                                             |              |               |                                                      |        |Total Price USD approx|Total Price GBP|
|                                                                               |   |                 |                  |                       |                    |                                                                             |              |               |                                                      |Items   |15.06                 |11.51          |
|                                                                               |   |                 |                  |                       |                    |                                                                             |              |               |                                                      |Shipping|20.28                 |15.5           |
|                                                                               |   |                 |                  |                       |                    |                                                                             |              |               |                                                      |Finnal  |35.34                 |27.01          |
