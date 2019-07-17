# -*- coding: utf-8 -*-

"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = '3liz'
__date__ = '2019-02-15'
__copyright__ = '(C) 2019 by 3liz'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from PyQt5.QtCore import QCoreApplication
from qgis.core import (
    QgsVectorLayer,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingContext,
    QgsProcessingUtils,
    QgsProcessingException,
    QgsProcessingParameterEnum,
    QgsProcessingParameterString,
    QgsProcessingOutputString,
    QgsProcessingOutputNumber,
    QgsProcessingOutputVectorLayer
)
from .tools import *
from processing.tools import postgis

class GetDataAsLayer(QgsProcessingAlgorithm):
    """

    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    CONNECTION_NAME = 'CONNECTION_NAME'

    OUTPUT_STATUS = 'OUTPUT_STATUS'
    OUTPUT_STRING = 'OUTPUT_STRING'
    OUTPUT_LAYER = 'OUTPUT_LAYER'
    OUTPUT_LAYER_NAME = 'OUTPUT_LAYER_NAME'

    SQL = 'SELECT * FROM gobs.indicator'
    LAYER_NAME = ''
    GEOM_FIELD = None

    def name(self):
        return 'get_data_as_layer'

    def displayName(self):
        return self.tr('Get data as layer')

    def group(self):
        return self.tr('Tools')

    def groupId(self):
        return 'gobs_tools'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return self.__class__()

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        # INPUTS

        # Database connection parameters
        db_param = QgsProcessingParameterString(
            self.CONNECTION_NAME, 'PostgreSQL connection',
            defaultValue='gobs',
            optional=False
        )
        db_param.setMetadata({
            'widget_wrapper': {
                'class': 'processing.gui.wrappers_postgis.ConnectionWidgetWrapper'
            }
        })
        self.addParameter(db_param)

        # Name of the layer
        self.addParameter(
            QgsProcessingParameterString(
                self.OUTPUT_LAYER_NAME, self.tr('Name of the output layer'),
                optional=True
            )
        )

        # OUTPUTS
        # Add output for status (integer)
        self.addOutput(
            QgsProcessingOutputNumber(
                self.OUTPUT_STATUS, self.tr('Output status')
            )
        )
        # Add output for message
        self.addOutput(
            QgsProcessingOutputString(
                self.OUTPUT_STRING, self.tr('Output message')
            )
        )

        # Output vector layer
        self.addOutput(
            QgsProcessingOutputVectorLayer(
                self.OUTPUT_LAYER, self.tr('Output layer')
            )
        )


    def setSql(self, parameters, context, feedback):

        self.SQL = self.SQL.replace('\n', ' ').rstrip(';')

    def setLayerName(self, parameters, context, feedback):
        output_layer_name = parameters[self.OUTPUT_LAYER_NAME]

        self.LAYER_NAME = output_layer_name


    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        connexion_name = parameters[self.CONNECTION_NAME]

        msg = ''
        status = 1

        # Set SQL
        self.setSql(parameters, context, feedback)
        # Set output layer name
        self.setLayerName(parameters, context, feedback)

        # Buid QGIS uri to load layer
        id_field = 'id'
        uri = postgis.uri_from_name(connexion_name)
        uri.setDataSource("", "(" + self.SQL + ")", self.GEOM_FIELD, "", id_field)
        vlayer = QgsVectorLayer(uri.uri(), "layername", "postgres")
        if not vlayer.isValid():
            feedback.pushInfo(
                self.tr('SQL = \n' + self.SQL)
            )
            raise QgsProcessingException(self.tr("""This layer is invalid!
                Please check the PostGIS log for error messages."""))

        # Load layer
        context.temporaryLayerStore().addMapLayer(vlayer)
        context.addLayerToLoadOnCompletion(
            vlayer.id(),
            QgsProcessingContext.LayerDetails(
                self.LAYER_NAME,
                context.project(),
                self.OUTPUT_LAYER
            )
        )

        return {
            self.OUTPUT_STATUS: status,
            self.OUTPUT_STRING: msg,
            self.OUTPUT_LAYER: vlayer.id()
        }