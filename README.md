# Bitcoin.de Price Indicator Applet

This indicator shows the current price of a Bitcoin in Euro from Bitcoin.de. 
The price updates automatically every 5 minutes. Update can also be triggered manually by pressing the update item from the menu. 
It also shows the last update timestamp and  in trouble of internet connection a timeout advice. There is also a menu item,
which opens bitcoin.de in your favourite browser. The link contains my id of the partner programme. If you click this item and 
register on bitcoin.de, I will get for a half year a 10% commission of the transaction fee, if you deal with bitcoins. This commission 
is paid by bitcoin.de, so you won't pay more as if you register directly.  

## Features
This indicator shows the current price of a bitcoin from bitcoin.de.

![Indicator Screenshot](https://raw.githubusercontent.com/Guenzn/bitcoin-de-indicator/master/img/indicator-screenshot.png)


## Installation

Create and change to a directory of your choice, where you want to install the indicator (e.g. in your home directory in a folder called indicators)

`cd ~`

`mkdir indicators`

`cd indicators`

Clone the sourcecode from Github

`git clone https://github.com/Guenzn/bitcoin-de-indicator.git`

Run setup to create a desktop file and a startup file, to let the indicator run when you login

`cd bitcoin-de-indicator`

`/bin/bash setup.sh`


## Roadmap

- Extend the setup script to be interactive, so that the user can remove the indicator from autostart and/or applications
- Translations
- Configure language, update interval, price trigger e.g.
- Integration of the user api


## Contribute

If you have any questions or ideas for new features, feel free to contribute by forking this repository or contacting me. 


## Donate
You like this indicator? It would be great if you spend me a coffee via PayPal ;) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BXP564QB2F27E)
