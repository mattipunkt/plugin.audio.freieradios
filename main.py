# -*- coding: utf-8 -*-
import sys, os
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import xbmcaddon

ADDON_ID      	= 'plugin.audio.freieradios'
SETTINGS 		= xbmcaddon.Addon(id=ADDON_ID)
ADDON_PATH    	= SETTINGS.getAddonInfo('path')	# Basis-Pfad Addon

def PLog(msg, loglevel=xbmc.LOGDEBUG):
#	if DEBUG == 'false':
#		return
	if isinstance(msg, str):		# entf. mit six
		msg = msg.encode('utf-8')
	loglevel = xbmc.LOGNOTICE
	# PLog('loglevel: ' + str(loglevel))
	if loglevel >= 2:
		xbmc.log("%s --> %s" % ('madsters', msg), level=loglevel)
		
def R(fname, abs_path=False):	
	PLog('R(fname): %s' % fname); # PLog(abs_path)
	# PLog("ADDON_PATH: " + ADDON_PATH)
	if abs_path:
		try:
			# fname = '%s/resources/%s' % (PluginAbsPath, fname)
			path = os.path.join(ADDON_PATH,fname)
			return path
		except Exception as exception:
			PLog(str(exception))
	else:
		if fname.endswith('png'):	# Icons im Unterordner images
			fname = '%s/resources/images/%s' % (ADDON_PATH, fname)
			fname = os.path.abspath(fname)
			# PLog("fname: " + fname)
			return os.path.join(fname)
		else:
			fname = "%s/resources/%s" % (ADDON_NAME, fname)
			fname = os.path.abspath(fname)
			return fname 

ICON_BERMUDAFUNK    = R('icon_bermudafunk.png')
ICON_COLORADIO      = R('icon_coloradio.png')
ICON_FREEFM         = R('icon_freefm.png')
ICON_FREIERADIOCOO  = R('icon_freieradiocoop.png')
ICON_FREIESRADIOST  = R('icon_freiesradiostuttgart.png')
ICON_FREIESRADIOFR  = R('icon_freiesradiofreudenstadt.png')
ICON_FREIESRADIOKA  = R('icon_freiesradiokassel.png')
ICON_FREIESRADIONE  = R('icon_freiesradioneumuenster.png')
ICON_FREIESSENDERK  = R('icon_freiessenderkombinat.png')
ICON_FREIESRADIOWI  = R('icon_freiesradiowiesental.png')
ICON_FRRAPO         = R('icon_frrapo.png')
ICON_LOHRO          = R('icon_lohro.png')
ICON_LORAMUENCHEN   = R('icon_loramuenchen.png')
ICON_ONDA           = R('icon_onda.png')                           # KEIN LIVESTREAM
ICON_PIRADIO        = R('icon_piradio.png')                       # IST DAS SELBE WIE RADIO
ICON_QUERFUNK       = R('icon_querfunk.png')
ICON_RADIOBLAU      = R('icon_radioblau.png')
ICON_RADIOCORAX     = R('icon_radiocorax.png')
ICON_RADIODREYECKL  = R('icon_radiodreyeckland.png') 
ICON_RADIOFRATZ     = R('icon_radiofratz.png')
ICON_RADIOFREI      = R('icon_radiofrei.png')
ICON_RADIOFLORA     = R('icon_radioflora.png')
ICON_RADIOQUER      = R('icon_radioquer.png')
ICON_RADIOSLUBFURT  = R('icon_radioslubfurt.png')
ICON_RADIOT         = R('icon_radiot.png')
ICON_RADIOUNERHOER  = R('icon_radiounerhoert.png')
ICON_RADIOZ         = R('icon_radioz.png')
ICON_RUNDFUNKMEISS  = R('icon_rundfunkmeissner.png')
ICON_STHOERFUNK     = R('icon_sthoerfunk.png')
ICON_WUESTEWELLE    = R('icon_wuestewelle.png')

ADDONICON = R('addon.png')
BACKGROUNDRADIO     = R('backgroundradio.png')

ICON_AGORA = R('icon_agora.png')
ICON_CR944 = R('icon_cr944.png')
ICON_FREIESRADIOFREISTADT = R('icon_freiesradiofreistadt.png')
ICON_FREIRAD = R('icon_freirad.png')
ICON_FREIESRADIOSALZKAMMERGUT = R('icon_freiesradiosalzkammergut.png')
ICON_RADIOORANGE = R('icon_radioorange.png')
ICON_RADIOFABRIK = R('icon_radiofrabrik.png')
ICON_RADIOB138 = R('icon_radiob138.png')
ICON_FREEQUENNS = R('icon_radiofreequenns.png')
ICON_RADIOFRO = R('icon_radiofro.png')
ICON_RADIOHELSINKI = R('icon_radiohelsinki.png')


# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'bermuda.funk': [{'name': 'Livestream',
                       'thumb': ICON_BERMUDAFUNK,
                       'video': 'http://streaming.fueralle.org:8000/bermudafunk.ogg',
                       'genre': 'Rhein-Neckar'}
                     ],
             'coloRadio': [{'name': 'Livestream',
                       'thumb': ICON_COLORADIO,
                       'video': 'http://streaming.fueralle.org:8000/corax_128.mp3',
                       'genre': 'Sachsen'}
                     ],
             'freeFM': [{'name': 'Livestream',
                       'thumb': ICON_FREEFM,
                       'video': 'http://stream.freefm.de:7000/Studio',
                       'genre': 'Ulm'}
                     ],
            'Freie Radio Cooperative': [{'name': 'Livestream',
                       'thumb': ICON_FREIERADIOCOO,
                       'video': 'http://stream.freefm.de:7000/Studio',
                       'genre': 'Husum'}
                     ],
            'Freies Radio Stuttgart': [{'name': 'Livestream',
                       'thumb': ICON_FREIESRADIOST,
                       'video': 'http://streaming.fueralle.org:8000/frs-hi.mp3',
                       'genre': 'Stuttgart'}
                     ],
            'Freies Radio Freudenstadt': [{'name': 'Momentan kein Livestream verfügbar.',
                       'thumb': ICON_FREIESRADIOFR,
                       'video': 'http://streaming.fueralle.org:8000/frs-hi.mp3',
                       'genre': 'Freudenstadt'}
                     ],
            'Freies Radio Kassel': [{'name': 'Livestream.',
                       'thumb': ICON_FREIESRADIOKA,
                       'video': 'http://stream.freiesradio.org:8000/live.mp3',
                       'genre': 'Kassel'}
                     ],
            'Freies Radio Neumünster': [{'name': 'Livestream',
                       'thumb': ICON_FREIESRADIONE,
                       'video': 'http://streaming.fueralle.org:8000/frn',
                       'genre': 'Neumünster'}
                     ],
            'Freies Radio Wiesental': [{'name': 'Livestream',
                       'thumb': ICON_FREIESRADIOWI,
                       'video': 'http://88.99.63.244:8000/;stream.mp3',
                       'genre': 'Wiesental'}
                     ],
            'Freies Sender Kombinat': [{'name': 'Livestream',
                       'thumb': ICON_FREIESSENDERK,
                       'video': 'http://stream.fsk-hh.org:8000/fsk.ogg',
                       'genre': 'Wiesental'}
                     ],
            'Frrapó': [{'name': 'Livestream',
                       'thumb': ICON_FRRAPO,
                       'video': 'http://ice.rosebud-media.de:8000/88vier',
                       'genre': 'Potsdamm'}
                     ],
            'LOHRO': [{'name': 'Livestream',
                       'thumb': ICON_LOHRO,
                       'video': 'http://stream.lohro.de:8000/lohro.mp3',
                       'genre': 'Rostock'}
                     ],
            'LoRa': [{'name': 'Livestream',
                       'thumb': ICON_LORAMUENCHEN,
                       'video': 'http://live.lora924.de:8000/lora-hq.mp3',
                       'genre': 'München'}
                     ],
            'Onda': [{'name': 'Livestream',
                       'thumb': ICON_ONDA,
                       'video': 'http://live.lora924.de:8000/lora-hq.mp3',
                       'genre': 'Berlin'}
                     ],
            'PiRadio': [{'name': 'Livestream',
                       'thumb': ICON_PIRADIO,
                       'video': 'http://ice.rosebud-media.de:8000/88vier',
                       'genre': 'Berlin'}
                     ],
            'Querfunk': [{'name': 'Livestream',
                       'thumb': ICON_QUERFUNK,
                       'video': 'http://mp3.querfunk.de/qfhi',
                       'genre': 'Karlsruhe'}
                     ],
            'Radio Blau': [{'name': 'Livestream',
                       'thumb': ICON_RADIOBLAU,
                       'video': 'http://radioblau.hoerradar.de/radioblau',
                       'genre': 'Leipzig'}
                     ],
            'Radio Corax': [{'name': 'Livestream',
                       'thumb': ICON_RADIOCORAX,
                       'video': 'http://listen.radiocorax.de/corax_192.mp3',
                       'genre': 'Halle'}
                     ],
            'Radio Dreyeckland': [{'name': 'Livestream',
                       'thumb': ICON_RADIODREYECKL,
                       'video': 'http://listen.radiocorax.de/corax_192.mp3',
                       'genre': 'Freiburg'}
                     ],
            'Radio Fratz': [{'name': 'Livestream',
                       'thumb': ICON_RADIOFRATZ,
                       'video': 'http://stream.radio-fratz.de:8000/stream.mp3',
                       'genre': 'Flensburg'}
                     ],
            'Radio Frei': [{'name': 'Livestream',
                       'thumb': ICON_RADIOFREI,
                       'video': 'http://streaming.fueralle.org/Radio-F.R.E.I',
                       'genre': 'Erfurt'}
                     ],
            'Radio Flora': [{'name': 'Livestream',
                       'thumb': ICON_RADIOFLORA,
                       'video': 'http://radioflora.de:8000/stream/live192.mp3?hash=1580484727882.mp3',
                       'genre': 'Hannover'}
                     ],
            'Radio Quer': [{'name': 'Livestream',
                       'thumb': ICON_RADIOQUER,
                       'video': 'http://radioflora.de:8000/stream/live192.mp3?hash=1580484727882.mp3',
                       'genre': 'Mainz'}
                     ],
            'Slubfurt': [{'name': 'Livestream',
                       'thumb': ICON_RADIOSLUBFURT,
                       'video': 'http://streaming.fueralle.org:8000/slubfurt',
                       'genre': 'Frankfurt (Oder) / Słubice'}
                     ],
            'Radio T': [{'name': 'Livestream',
                       'thumb': ICON_RADIOT,
                       'video': 'http://listen.radiot.de/radiot_192.mp3',
                       'genre': 'Chemnitz'}
                     ],
            'Radio Unerhört': [{'name': 'Livestream',
                       'thumb': ICON_RADIOUNERHOER,
                       'video': 'http://stream.radio-rum.de:8000/rum.mp3',
                       'genre': 'Marburg'}
                     ],
            'Radio Z': [{'name': 'Livestream',
                       'thumb': ICON_RADIOZ,
                       'video': 'http://snd.radio-z.net:8000/Radio-Z',
                       'genre': 'Nürnberg'}
                     ],
            'Rundfunk Meissner': [{'name': 'Momentan kein Livestream verfügbar',
                       'thumb': ICON_RUNDFUNKMEISS,
                       'video': 'http://snd.radio-z.net:8000/Radio-Z',
                       'genre': 'Eschwege'}
                     ],
            'St(H)örfunk': [{'name': 'Livestream',
                       'thumb': ICON_STHOERFUNK,
                       'video': 'http://stream.sthoerfunk.de:7000/sthoerfunk.mp3',
                       'genre': 'Schwäbisch Hall'}
                     ],
            'Wüste Welle': [{'name': 'Momentan kein Livestream verfügbar',
                       'thumb': ICON_WUESTEWELLE,
                       'video': 'http://stream.sthoerfunk.de:7000/sthoerfunk.mp3',
                       'genre': 'Tübingen'}
                     ]}
                   

SENDERAT = {'Agora': [{'name': 'Livestream',
                       'thumb': ICON_AGORA,
                       'video': 'http://livestream.agora.at/agora',
                       'genre': 'Klagenfurt/Celovec'}
                     ],
           'Campus & Cityradio 94.4': [{'name': 'Livestream',
                       'thumb': ICON_CR944,
                       'video': 'http://www.cr944.at:8000/cr944-ogg',
                       'genre': 'Pölten'}
                     ],
           'Freies Radio Freistadt': [{'name': 'Livestream',
                       'thumb': ICON_FREIESRADIOFREISTADT,
                       'video': 'https://develop.servus.at:8443/frfg',
                       'genre': 'Freistadt'}
                     ],
           'FREIRAD': [{'name': 'Livestream',
                       'thumb': ICON_FREIRAD,
                       'video': 'http://stream.freirad.at:8002/live.mp3',
                       'genre': 'Innsbruck'}
                     ],
           'Freies Radio Salzkammergut': [{'name': 'Livestream',
                       'thumb': ICON_FREIESRADIOSALZKAMMERGUT,
                       'video': 'http://stream.xaok.org:8000/frs.mp3',
                       'genre': 'Salzkammergut'}
                     ],
           'Radio Ypsilon': [{'name': 'Momentan kein Livestream verfügbar.',
                       'thumb': ADDONICON,
                       'video': 'http://live.radioypsilon.at:85/broadwave.mp3',
                       'genre': 'Hollabrunn'}
                     ],
           'Radio OP': [{'name': 'Momentan kein Livestream verfügbar.',
                       'thumb': ADDONICON,
                       'video': 'http://live.radioypsilon.at:85/broadwave.mp3',
                       'genre': 'Oberpullendorf'}
                     ],
           'Orange 94.0': [{'name': 'Livestream',
                       'thumb': ICON_RADIOORANGE,
                       'video': 'http://stream.o94.at:8000/live.mp3',
                       'genre': 'Wien'}
                     ],
           'PROTON - das freie Radio': [{'name': 'Livestream',
                       'thumb': ADDONICON,
                       'video': 'http://radioproton.at:8000/proton',
                       'genre': 'Wien'}
                     ],
           'Radiofabrik': [{'name': 'Livestream',
                       'thumb': ICON_RADIOFABRIK,
                       'video': 'https://stream.radiofabrik.at/rf_low.mp3',
                       'genre': 'Salzburg'}
                     ],
           'Radio Freequenns': [{'name': 'Livestream',
                       'thumb': ICON_FREEQUENNS,
                       'video': 'http://livestream.freequenns.at/live',
                       'genre': 'Ennstal'}
                     ],
           'Radio FRO': [{'name': 'Livestream',
                       'thumb': ICON_RADIOFRO,
                       'video': 'https://stream.fro.at/fro-128.ogg',
                       'genre': 'Linz'}
                     ],
           'Radio Helsinki': [{'name': 'Livestream',
                       'thumb': ICON_RADIOHELSINKI,
                       'video': 'https://live.helsinki.at:8088/live160.ogg',
                       'genre': 'Graz'}
                     ]}



if SETTINGS.getSetting('country') == 'false':
    def get_url(**kwargs):

        """
        Create a URL for calling the plugin recursively from the given set of keyword arguments.

        :param kwargs: "argument=value" pairs
        :type kwargs: dict
        :return: plugin call URL
        :rtype: str
   	    """
        return '{0}?{1}'.format(_url, urlencode(kwargs))


    def get_categories():
        """
        Get the list of video categories.

        Here you can insert some parsing code that retrieves
        the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
        from some site or server.

        .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

        :return: The list of video categories
        :rtype: types.GeneratorType
        """
        return VIDEOS.iterkeys()



    def get_videos(category):
        """
 	    Get the list of videofiles/streams.

        Here you can insert some parsing code that retrieves
        the list of video streams in the given category from some site or server.

        .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

        :param category: Category name
        :type category: str
        :return: the list of videos in the category
        :rtype: list
        """
        return VIDEOS[category]


    def list_categories():
        """
        Create the list of video categories in the Kodi interface.
        """
        # Set plugin category. It is displayed in some skins as the name
        # of the current section.
        xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
        # Set plugin content. It allows Kodi to select appropriate views
        # for this type of content.
        xbmcplugin.setContent(_handle, 'videos')
        # Get video categories
        categories = get_categories()
        # Iterate through categories
        for category in categories:
        # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
            list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                              'icon': VIDEOS[category][0]['thumb'],
                              'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
            list_item.setInfo('video', {'title': category,
                                        'genre': category,
                                        'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
            url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
            is_folder = True
        # Add our item to the Kodi virtual folder listing.
            xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
        # Add a sort method for the virtual folder items (alphabetically, ignore articles)
            xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(_handle)


    def list_videos(category):
        """
        Create the list of playable videos in the Kodi interface.

        :param category: Category name
        :type category: str
        """
        # Set plugin category. It is displayed in some skins as the name
        # of the current section.
        xbmcplugin.setPluginCategory(_handle, category)
        # Set plugin content. It allows Kodi to select appropriate views
        # for this type of content.
        xbmcplugin.setContent(_handle, 'videos')
        # Get the list of videos in the category.
        videos = get_videos(category)
        # Iterate through videos.
        for video in videos:
        # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
            list_item.setInfo('video', {'title': video['name'],
                                        'genre': video['genre'],
                                        'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
            list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
         # This is mandatory for playable items!
            list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
            url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
            is_folder = False
        # Add our item to the Kodi virtual folder listing.
            xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
        # Add a sort method for the virtual folder items (alphabetically, ignore articles)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(_handle)


    def play_video(path):
        """
        Play a video by the provided path.

        :param path: Fully-qualified video URL
        :type path: str
        """
        # Create a playable item with a path to play.
        play_item = xbmcgui.ListItem(path=path)
        # Pass the item to the Kodi player.
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

		
    def router(paramstring):
        """
        Router function that calls other functions
        depending on the provided paramstring

        :param paramstring: URL encoded plugin paramstring
        :type paramstring: str
        """
        # Parse a URL-encoded paramstring to the dictionary of
        # {<parameter>: <value>} elements
        params = dict(parse_qsl(paramstring))
        # Check the parameters passed to the plugin
        if params:
            if params['action'] == 'listing':
            # Display the list of videos in a provided category.
                list_videos(params['category'])
            elif params['action'] == 'play':
            # Play a video from a provided URL.
                play_video(params['video'])
            else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
                raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
        else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
            list_categories()


    if __name__ == '__main__':
        # Call the router function and pass the plugin call parameters to it.
        # We use string slicing to trim the leading '?' from the plugin call paramstring
        PLog(sys.argv[2])
        router(sys.argv[2][1:])


else:
    def get_url(**kwargs):
        """
        Create a URL for calling the plugin recursively from the given set of keyword arguments.

        :param kwargs: "argument=value" pairs
        :type kwargs: dict
        :return: plugin call URL
        :rtype: str
        """
        return '{0}?{1}'.format(_url, urlencode(kwargs))


    def get_categories():
        """
        Get the list of video categories.

        Here you can insert some parsing code that retrieves
        the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
        from some site or server.

        .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

        :return: The list of video categories
        :rtype: types.GeneratorType
        """
        return SENDERAT.iterkeys()



    def get_videos(category):
        """
           Get the list of videofiles/streams.

        Here you can insert some parsing code that retrieves
        the list of video streams in the given category from some site or server.

        .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

        :param category: Category name
        :type category: str
        :return: the list of videos in the category
        :rtype: list
        """
        return SENDERAT[category]


    def list_categories():
        """
        Create the list of video categories in the Kodi interface.
        """
        # Set plugin category. It is displayed in some skins as the name
        # of the current section.
        xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
        # Set plugin content. It allows Kodi to select appropriate views
        # for this type of content.
        xbmcplugin.setContent(_handle, 'SENDERAT')
        # Get video categories
        categories = get_categories()
        # Iterate through categories
        for category in categories:
        # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
            list_item.setArt({'thumb': SENDERAT[category][0]['thumb'],
                              'icon': SENDERAT[category][0]['thumb'],
                              'fanart': SENDERAT[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
            list_item.setInfo('video', {'title': category,
                                        'genre': category,
                                        'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
            url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
            is_folder = True
        # Add our item to the Kodi virtual folder listing.
            xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
        # Add a sort method for the virtual folder items (alphabetically, ignore articles)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(_handle)


    def list_videos(category):
        """
        Create the list of playable videos in the Kodi interface.

        :param category: Category name
        :type category: str
        """
        # Set plugin category. It is displayed in some skins as the name
        # of the current section.
        xbmcplugin.setPluginCategory(_handle, category)
        # Set plugin content. It allows Kodi to select appropriate views
        # for this type of content.
        xbmcplugin.setContent(_handle, 'videos')
        # Get the list of videos in the category.
        videos = get_videos(category)
        # Iterate through videos.
        for video in videos:
        # Create a list item with a text label and a thumbnail image.
            list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
            list_item.setInfo('video', {'title': video['name'],
                                        'genre': video['genre'],
                                        'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
            list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
         # This is mandatory for playable items!
            list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
            url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
            is_folder = False
        # Add our item to the Kodi virtual folder listing.
            xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
        # Add a sort method for the virtual folder items (alphabetically, ignore articles)
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        # Finish creating a virtual folder.
        xbmcplugin.endOfDirectory(_handle)


    def play_video(path):
        """
        Play a video by the provided path.

        :param path: Fully-qualified video URL
        :type path: str
        """
        # Create a playable item with a path to play.
        play_item = xbmcgui.ListItem(path=path)
        # Pass the item to the Kodi player.
        xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

        
    def router(paramstring):
        """
        Router function that calls other functions
        depending on the provided paramstring

        :param paramstring: URL encoded plugin paramstring
        :type paramstring: str
        """
        # Parse a URL-encoded paramstring to the dictionary of
        # {<parameter>: <value>} elements
        params = dict(parse_qsl(paramstring))
        # Check the parameters passed to the plugin
        if params:
            if params['action'] == 'listing':
            # Display the list of videos in a provided category.
                list_videos(params['category'])
            elif params['action'] == 'play':
            # Play a video from a provided URL.
                play_video(params['video'])
            else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
                raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
        else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
            list_categories()


    if __name__ == '__main__':
        # Call the router function and pass the plugin call parameters to it.
        # We use string slicing to trim the leading '?' from the plugin call paramstring
        PLog(sys.argv[2])
        router(sys.argv[2][1:])