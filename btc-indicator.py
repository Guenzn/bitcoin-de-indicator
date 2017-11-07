#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2017 Günter Selbert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import webbrowser

import requests

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GObject as gobject
from gi.repository import GdkPixbuf as gdkpixbuf

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
ICON = WORKING_DIRECTORY + '/img/indicator-icon.png'
LOGO = WORKING_DIRECTORY + '/img/bitcoin-logo.png'
INDICATOR_INIT_LABEL = "-"
LOCALE = "de"
UPDATEITEM_INIT_LABEL = "Initializing..."
BITCOIN_DE_API_URL = "https://bitcoinapi.de/widget/current-btc-price/rate.json?culture=" + LOCALE
BITCOIN_DE_AFFILIATE_URL = 'https://www.bitcoin.de/de/r/ssf5ch'
PAYPAL_DONATE_URL = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=BXP564QB2F27E"


class BitcoinDeLogic(object):

    api_url = ""
    fallback_response = {'price_eur': INDICATOR_INIT_LABEL, 'date_de': '-'}

    def get_data_json(self, *args, **kwargs):
        try:
            response = requests.get(BITCOIN_DE_API_URL, timeout=5).json()
            self.fallback_response = response
        except:
            response = self.fallback_response.copy()
            response['date_de'] += " (Connection Timeout)"
        return response

    def update(self, *args, **kwargs):
        item_update.set_label("Updating...")

        json_obj = self.get_data_json()
        price_eur = json_obj['price_eur'] #.replace('\u20ac', '')
        date_de = json_obj['date_de']

        indicator.set_label(price_eur, "100%")
        item_update.set_label("Updated at {}".format(date_de))
        return True


class BitcoinDeIndicator(object):

    logic = None

    def __init__(self, logic, *args, **kwargs):
        self.logic = logic

        global indicator
        indicator = appindicator.Indicator.new("bitcoin-de-indicator", ICON, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_label(INDICATOR_INIT_LABEL, '100%')
        indicator.set_menu(self.create_menu())

        # Update 5 minutes
        gobject.timeout_add(1000 * 60 * 5, self.update)

        self.update()
        gtk.main()

    def create_menu(self, *args, **kwargs):
        menu = gtk.Menu()

        global item_update
        item_update = gtk.MenuItem('Initializing...')
        item_update.connect('activate', self.update)
        menu.append(item_update)

        item_website = gtk.MenuItem('Open Bitcoin.de')
        item_website.connect('activate', self.website)
        menu.append(item_website)

        menu.append(gtk.SeparatorMenuItem())

        item_about = gtk.MenuItem('About')
        item_about.connect('activate', self.about)
        menu.append(item_about)

        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def update(self, *args, **kwargs):
        self.logic.update()
        return True

    def website(self, *args, **kwargs):
        webbrowser.open_new_tab(BITCOIN_DE_AFFILIATE_URL)

    def about(self, *args, **kwargs):
        ad = gtk.AboutDialog()

        ad.set_logo(gdkpixbuf.Pixbuf.new_from_file(LOGO))
        ad.set_program_name("Bitcoin.de BTC-EUR Indicator")
        ad.set_comments("Shows the current Bitcoin price in EUR from bitcoin.de.\nNote: There is a link to the website of bitcoin.de, which includes my id of the partner programme.\n\nThis Indicator was implemented and tested on Linux Ubuntu 16.04 LTS with Unity (needs Python 3.5).")

        ad.set_version("1.0.0")
        ad.set_copyright("Copyright 2017 Günter Selbert")

        ad.set_license("MIT License\n\nCopyright (c) 2017 Günter Selbert\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
        ad.set_wrap_license(True)
        ad.set_website(PAYPAL_DONATE_URL)
        ad.set_website_label("Donate (Paypal)")

        ad.run()
        ad.destroy()

    def quit(self, *args, **kwargs):
        gtk.main_quit()


if __name__ == "__main__":
    BitcoinDeIndicator(BitcoinDeLogic())