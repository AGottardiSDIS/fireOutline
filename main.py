"""
The main module
"""
import os

from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer, QgsMessageLog
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QTextCharFormat
from PyQt5.QtWidgets import QAction, QFileDialog
from .constants import MessageType, CrsType, ImagePriority, ImageFormat, BaseUrl, ExtentType, ServiceType, TimeType, \
    AVAILABLE_SERVICE_TYPES, COVERAGE_MAX_BBOX_SIZE, ACTION_COOLDOWN, VECTOR_LAYER_COLOR_OPACITY
from .dockwidget import SentinelHubDockWidget
from .exceptions import show_message, action_handler, LayerValidator, ResolutionValidator, ExtentValidator, \
    DownloadFolderValidator, BBoxTransformError
from .sentinelhub.configuration import ConfigurationManager
from .sentinelhub.client import Client
from .sentinelhub.ogc import get_service_uri
from .sentinelhub.user import get_username
from .sentinelhub.wcs import download_wcs_image
from .sentinelhub.wfs import get_cloud_cover
from .settings import Settings
from .utils.common import is_float_or_undefined
from .utils.geo import get_bbox, is_bbox_too_large, bbox_to_string, get_custom_bbox, is_current_map_crs
from .utils.map import get_qgis_layers, set_layer_fill_color_opacity
from .utils.meta import get_plugin_version, PLUGIN_NAME
from .utils.naming import get_qgis_layer_name
from .utils.time import parse_date, get_month_time_interval

class FireOutline:
	 def __init__(self, iface):
        """ Called by QGIS at the beginning when you open QGIS or when the plugin is enabled in the
        Plugin Manager.

        :param iface: A QGIS interface instance, it is the same object as qgis.utils.iface
        :type iface: QgsInterface
        """
        self.iface = iface