#!/usr/bin/env bash

DESKTOP_FILE=~/.local/share/applications/bitcoin-de-indicator.desktop
STARTUP_FILE=~/.config/autostart/bitcoin-de-indicator.desktop
INDICATOR_DIRECTORY=${PWD}

echo -e "Creating app entry for unity dash..."

echo "[Desktop Entry]" > $DESKTOP_FILE
echo "Icon=$INDICATOR_DIRECTORY/img/bitcoin-logo.png" >> $DESKTOP_FILE
echo "Name=Bitcoin.de Price Indicator" >> $DESKTOP_FILE
echo "Comment=Indicator Applet to show the price of a Bitcoin from bitcoin.de" >> $DESKTOP_FILE
echo "Exec=python3.5 $INDICATOR_DIRECTORY/btc-indicator.py" >> $DESKTOP_FILE
echo "Terminal=false" >> $DESKTOP_FILE
echo "Type=Application" >> $DESKTOP_FILE
echo "Categories=Utility;TrayIcon;" >> $DESKTOP_FILE
echo "Keywords=Bitcoin,Bitcoin.de,Crypto" >> $DESKTOP_FILE
echo "OnlyShowIn=GNOME;KDE;LXDE;LXQt;MATE;Razor;ROX;TDE;Unity;XFCE;EDE;Cinnamon;Pantheon;" >> $DESKTOP_FILE
echo "StartupNotify=false" >> $DESKTOP_FILE
echo "Name[de_DE]=Bitcoin.de Preis Indicator" >> $DESKTOP_FILE
echo "GenericName[de_DE]=Ein simples Bitcoin.de-Preis Indikatorapplet" >> $DESKTOP_FILE
echo "Comment[de_DE]=Zeigt den aktuellen Bitcoin.de Kurs an" >> $DESKTOP_FILE
chmod +x $DESKTOP_FILE

echo -e "Creating autostart entry..."
mkdir -p ~/.config/autostart
echo "[Desktop Entry]" > $STARTUP_FILE
echo "Type=Application" >> $STARTUP_FILE
echo "Exec=python3.5 $INDICATOR_DIRECTORY/btc-indicator.py" >> $STARTUP_FILE
echo "Icon=$INDICATOR_DIRECTORY/img/bitcoin-logo.png" >> $STARTUP_FILE
echo "Comment=Bitcoin.de Price Indicator" >> $STARTUP_FILE
echo "X-GNOME-Autostart-enabled=true" >> $STARTUP_FILE

echo -e "Setup done, log out to see changes..."